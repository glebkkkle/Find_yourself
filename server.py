from llama_cpp import Llama
from rag import RAG
llm=Llama(model_path="/mnt/c/Users/klyme/Downloads/gemma-3-finetune.Q8_0.gguf", n_gpu_layers=-1, n_ctx=4096, n_batch=512)

class Model():
    def __init__(self, model_path):
        self.model=Llama(model_path=model_path, n_ctx=4096, n_gpu_layers=-1)
    
    def __call__(self):
        return
    


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

    output = llm(prompt, max_tokens=2048, stop=[]) 
    text = output["choices"][0]["text"]

    return jsonify({"response": text.strip()})

@app.route("/check_data", methods=["POST"])
def receive_data():
    data=request.get_json()
    print(data)
    print(type(data))

    prompt=data.get("prompt", "")

    return jsonify({'response' : prompt})

helper=RAG()

@app.route("/majors",methods=["POST"])
def find_suitable_major():
    data=request.get_json()
    prompt=data.get("prompt", "")

    found_major=helper(prompt)
    return jsonify({"response" : found_major})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
