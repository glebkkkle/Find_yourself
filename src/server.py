from llama_cpp import Llama
from quiz_majors import llm, run_chatbot, profile_gen_prompt,pick_major_question, pick_question, update_major_weights, update_cluster_weights, softmax, init_major_scores, output_major_suggestion
from agent_chat import instance

from flask import Flask, request, jsonify
from flask_cors import CORS

sessions = {}
app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return "Health check"


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    prompt=profile_gen_prompt + ' ' + prompt
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


@app.route("/start_cluster_quiz", methods=["POST"])
def start_quiz():
    user_id = request.json["user_id"]
    sessions[user_id]={
        'quiz_stage':'cluster', 
        'cluster_scores':{'STEM_data':0, 'Business':0, 'Humanities':0, 'STEM_engineering':0},
        'major_scores':None, 
        'current_major':None, 
        'current_mid':None, 

    }
    q, opts, qid, cluster = pick_question(sessions[user_id]["cluster_scores"])

    sessions[user_id]['current_cluster'] =cluster 
    sessions[user_id]['current_qid']=qid
    
    return {"stage": "cluster", "question": q, "options": opts}


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
            
            state['current_mid']=new_mid
            state['current_major']=major

            return {"stage": "major", "question": q, "options": opts}
        
        else:
            q, opts, new_qid, cluster = pick_question(state["cluster_scores"])
            state['current_qid']=new_qid
            state['current_cluster']=cluster

            return {"stage": cluster, "question": q, "options": opts}

    elif state["quiz_stage"] == "major":
        # update major scores...
        state["major_scores"] = softmax(update_major_weights(
            state["current_cluster"], mid, user_answer, major, state["major_scores"]
        ))

        if any(s >= 0.65 for s in state["major_scores"].values()):
            final_major = max(state["major_scores"], key=state["major_scores"].get)
            return {"stage": "done", "result": final_major}
        else:
            q, opts, new_mid, major = pick_major_question(state["major_scores"], state["current_cluster"])
            if q is None or opts is None:

                print('No questions left')

            state['current_mid']=new_mid
            state['current_major']=major

            return {"stage": "major", "question": q, "options": opts}



@app.route('/suggest_major', methods=['POST'])
def suggest_m():
    user_profile=request.json['profile']
    user_major_description=request.json['major']
    
    model_suggestion=output_major_suggestion(llm, user_profile, user_major_description)
    
    return {'text':model_suggestion}


@app.route('/chat', methods=['POST'])
def run_model():
    _, query=request.json['session_id'], request.json['query']

    r=run_chatbot(query)

    return {'ai_m':r}


var=' '

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

