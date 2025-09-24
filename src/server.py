from llama_cpp import Llama

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




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
