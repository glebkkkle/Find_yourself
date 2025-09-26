from llama_cpp import Llama
from quiz_majors import pick_major_question, pick_question, update_major_weights, update_cluster_weights, softmax, init_major_scores


llm=Llama(model_path="/mnt/c/Users/klyme/Downloads/gemma-3-finetune.Q8_0.gguf", n_gpu_layers=-1, n_ctx=4096, n_batch=512)
initial_prompt="You are given a set of quiz answers from a person. Based on these answers, generate a coherent profile of the person that follows the structure: (1) Your Hard Skills – summarize technical strengths with explicit reference to supporting question numbers, (2) Your Soft Skills – summarize interpersonal/emotional/adaptive strengths with explicit reference to supporting question numbers, (3) Your Overall Profile – provide a friendly yet formal summary combining hard and soft skills, highlighting tendencies and weaker inclinations with reference to answers, (4) Possible Career-Study Directions – suggest broad pathways (not narrow job titles) aligned to the student’s strengths, linked to answers where possible. The tone must be friendly and formal, and all sections must clearly explain how the answers informed the conclusions.The person's answers: "

class Model():
    def __init__(self, model_path):
        self.model=Llama(model_path=model_path, n_ctx=4096, n_gpu_layers=-1)
    
    def __call__(self):
        return
    

def output_major_suggestion(profile, major):
    llm=Llama(model_path="/mnt/c/Users/klyme/Downloads/codellama-7b-instruct.Q4_0.gguf", n_ctx=9000, n_batch=512, n_gpu_layers=-1)
    prompt=f"""You are an expert career advisor. Your task is to generate a personalized explanation of why a suggested college major suits a specific user. 

    Instructions:
    1. Read the user's profile carefully. Highlight their hard and soft skills, interests, and preferences.
    2. Read the description of the suggested major. Understand its technical requirements, soft skills needed, and potential career paths.
    3. Write a clear, professional summary that explains why the major fits the user. 
    4. Make explicit links between the user's strengths and aspects of the major.
    5. Use details from both inputs but summarize in 4-6 sentences. Avoid repeating the full description of the major.

    User Profile:
    {profile}

    Suggested Major:
    {major}

    Output:"""

    response=llm(prompt, max_tokens=2048, echo=False)
    llm.close()
    return response["choices"][0]['text']



from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return "Health check"


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    prompt=initial_prompt + ' ' + prompt
    output = llm(prompt, max_tokens=2048, stop=[]) 
    text = output["choices"][0]["text"]

    return jsonify({"response": text.strip()})



@app.route('/receive_q_a', methods=['POST'])
def q_a():
    data=request.get_json()
    question=data.get('q', '')
    answers=data.get('o', [])

    
    return jsonify({'question':question, 'answers':answers})


@app.route("/major_quiz", methods=['POST'])
def f():

    data=request.get_json()
    prompt=data.get('prompt', '')

    output=llm(prompt, max_tokens=2048)
    text=output['choices'][0]['text']

    return jsonify({"response":text.strip()})


@app.route("/check_data", methods=["POST"])
def receive_data():
    data=request.get_json()
    prompt=data.get("prompt", "")

    return jsonify({'response' : prompt})



@app.route("/majors",methods=["POST"])
def find_suitable_major():
    data=request.get_json()
    prompt=data.get("prompt", "")

    found_major=(prompt)
    return jsonify({"response" : found_major})

sessions = {
    "abc123": { 
        "quiz_stage": "cluster",              # "cluster" or "major" or "done"
        "cluster_scores": {                   # scores for cluster quiz
            "STEM_data": 0,
            "Business": 0,
            "Humanities": 0,
            "STEM_engineering": 0
        },
        "major_scores": None,                 # initialized later when cluster quiz ends
        "current_cluster": None,              # set when cluster quiz finishes
        "current_question_id": None           # optional: track which question was last sent
    }, 

    'new_user123':
    {
        'quiz_stage':'cluster', 
        'cluster_scores': {                   # scores for cluster quiz
            "STEM_data": 0,
            "Business": 0,
            "Humanities": 0,
            "STEM_engineering": 0
        },
     
        "major_scores": None,                 # initialized later when cluster quiz ends
        "current_cluster": None,              # set when cluster quiz finishes     
        'current_qid':None, 
        'current_mid':None, 
        'current_major':None, 

        
    },  

    
    }


@app.route("/start_cluster_quiz", methods=["POST"])
def start_quiz():
    user_id = request.json["user_id"]
    q, opts, qid, cluster = pick_question(sessions[user_id]["cluster_scores"])

    sessions[user_id] = {
        "quiz_stage": "cluster",
        "cluster_scores": {"STEM_data":0, "Business":0, "Humanities":0, "STEM_engineering":0},
        "major_scores": None,
        "current_cluster": cluster, 
        'current_qid':qid, 
        'current_major':None, 
        'current_mid':None,


    }

    return {"stage": "cluster", "question": q, "options": opts}


def start_major_quiz(user_id, major_scores, cluster, state):
    q, opt, mid, major=pick_major_question(major_scores, cluster)

    state['mid']=mid
    state['current_major']=major
    
    return state, q, opt


@app.route("/answer", methods=["POST"])
def answer():
    user_id = request.json["user_id"]
    user_answer=request.json['answer']
    state = sessions[user_id]
    qid=state['current_qid']
    mid=state['current_mid']
    major=state['current_major']
    cluster=state['current_cluster']


    if state["quiz_stage"] == "cluster":

        # update cluster scores...


        state["cluster_scores"] = softmax(update_cluster_weights(
            user_answer, qid, cluster, state["cluster_scores"]
        ))

        if any(s >= 0.65 for s in state["cluster_scores"].values()):
            state["quiz_stage"] = "major"
            state["current_cluster"] = max(state["cluster_scores"], key=state["cluster_scores"].get)
            state["major_scores"] = init_major_scores(state["current_cluster"])
            q, opts, new_mid, major = pick_major_question(state["major_scores"], state["current_cluster"])

            print('STOPPING THE CLUSTER QUIZ, GOING FOR A MAJOR QUIZ')
            print(state['major_scores'])
            
            state['current_mid']=new_mid
            state['current_major']=major

            return {"stage": "major", "question": q, "options": opts}
        
        else:
            q, opts, new_qid, cluster = pick_question(state["cluster_scores"])
            state['current_qid']=new_qid
            state['current_cluster']=cluster
            print(state)
            return {"stage": cluster, "question": q, "options": opts}

    elif state["quiz_stage"] == "major":
        # update major scores...
        state["major_scores"] = softmax(update_major_weights(
            state["current_cluster"], mid, user_answer, major, state["major_scores"]
        ))
        print(state['major_scores'])
        if any(s >= 0.65 for s in state["major_scores"].values()):
            final_major = max(state["major_scores"], key=state["major_scores"].get)
            print('DONE')
            print(final_major)
            return {"stage": "done", "result": final_major}
        else:
            q, opts, new_mid, major = pick_major_question(state["major_scores"], state["current_cluster"])
            print(new_mid)

            state['current_mid']=new_mid
            state['current_major']=major
            print(state)

            return {"stage": "major", "question": q, "options": opts}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

