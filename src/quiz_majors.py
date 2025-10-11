from  src.ds import STEM_data_cluster, Business_cluster, STEM_engineering_cluster, Humanities_cluster
import numpy as np 
from llama_cpp import Llama
import copy
model_path="/mnt/c/Users/klyme/Downloads/gemma-3-finetune.Q8_0.gguf"
sessions={}

def softmax(scores, temperature=0.5):
    keys = list(scores.keys()) 
    vals = np.array(list(scores.values()))
    
    exp_scores = np.exp(vals / temperature)   
    probs = exp_scores / np.sum(exp_scores)
    
    return dict(zip(keys, probs))

#pick cluster question
def pick_question(clusters,cluster_scores, alpha=None):
    dominant_cluster = max(cluster_scores, key=lambda x : cluster_scores[x])

    cluster_questions_list=clusters[dominant_cluster]['cluster_questions']
    
    for question_id in range(len(cluster_questions_list)):
        
        if not cluster_questions_list[question_id]['seen']:
            answer_options=cluster_questions_list[question_id]['answer_weights'].keys()
            lst=[*answer_options]
            clusters[dominant_cluster]['cluster_questions'][question_id]['seen']=True

            return cluster_questions_list[question_id]['question_text'], lst, question_id, dominant_cluster
        else:
            print('already seen question')
    #if no questions left, return none 

    return None, None, None, None

#pick major question
def pick_major_question(clusters,major_scores, cluster):
    dominant_major = max(major_scores, key=lambda x : major_scores[x])
    q_lst=clusters[cluster]['majors'][dominant_major]['major_questions']


    for major_id in range(len(q_lst)):

        if not q_lst[major_id]['seen']:
            clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['seen']=True
            q=clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['question_text']
            options=clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['answer_weights']
            
            return q, options, major_id, dominant_major

    
    return None, None, None, None

    
def update_cluster_weights(clusters,user_ans, cluster_id, cluster, cluster_scores, major_id=None):
    question = clusters[cluster]['cluster_questions'][cluster_id]
    answer_weight = question['answer_weights'][user_ans]

    for cl, base_weight in question['cluster_weights'].items():
        cluster_scores[cl] += base_weight * answer_weight

    return cluster_scores


def update_major_weights(clusters,cluster, major_id,user_ans,  major_name, major_scores):
    question=clusters[cluster]['majors'][major_name]['major_questions'][major_id]
    answer_weight=question['answer_weights'][user_ans]

    for mj, base_weight in question['major_weights'].items():
        major_scores[mj]+=base_weight * answer_weight

    return major_scores



def init_major_scores(cluster):
    major_scores = {
        'STEM_data': {'Data Science': 0, 'Artificial Intelligence': 0, 'Accounting': 0, 'Data Analytics': 0},
        'Business': {'Business Administration': 0, 'Economics': 0, 'Finance': 0, 'Management': 0},
        'Humanities': {'History': 0, 'Philosophy': 0, 'Linguistics': 0, 'International Relations': 0},
        'STEM_engineering': {'Mechanical Engineering': 0, 'Electrical Engineering': 0, 'Civil Engineering': 0, 'Biomedical Engineering': 0}
    }
    return major_scores[cluster].copy() 


class MainLLM:
    def __init__(self, model_path=model_path):
        self.llm=Llama(model_path, n_ctx=4096, n_gpu_layers=-1)

    def generate_user_profile(self, q_a):
        prompt=f"You are given a set of quiz answers from a person. Based on these answers, generate a coherent profile of the person that follows the structure: (1) Your Hard Skills – summarize technical strengths with explicit reference to supporting question numbers, (2) Your Soft Skills – summarize interpersonal/emotional/adaptive strengths with explicit reference to supporting question numbers, (3) Your Overall Profile – provide a friendly yet formal summary combining hard and soft skills, highlighting tendencies and weaker inclinations with reference to answers, (4) Possible Career-Study Directions – suggest broad pathways (not narrow job titles) aligned to the student’s strengths, linked to answers where possible. The tone must be friendly and formal, and all sections must clearly explain how the answers informed the conclusions.The person's answers: {q_a}"
        response=self.llm(prompt, max_tokens=4096, echo=False)

        return response['choices'][0]['text']
    
    def generate_major_suggestion(self, profile, major):
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

        Output: """

        response=self.llm(prompt, max_tokens=2048, echo=False)

        return response["choices"][0]['text']


    def run_chatbot(self,query):
        prompt='You are a helpul chat-assistant bot. Answer to user politely and carefuly'
        response=self.llm(prompt+query, max_tokens=4096)['choices'][0]['text']

        return response

class RunPremiumQuizMain:
    def __init__(self, session_id):
        self.init_quiz(session_id)
        self.session_id = session_id
        self.done=False
        self.final_major=None

    def init_quiz(self, session_id):
        """Initialize a new quiz session."""
        self.clusters={}

        self.clusters['STEM_data']=copy.deepcopy(STEM_data_cluster)
        self.clusters['Business']=copy.deepcopy(Business_cluster)

        self.clusters['Humanities']=copy.deepcopy(Humanities_cluster)
        self.clusters['STEM_engineering']=copy.deepcopy(STEM_engineering_cluster)

        sessions[session_id] = {
            'quiz_stage': 'cluster',
            'cluster_scores': {'STEM_data':0, 'Business':0, 'Humanities':0, 'STEM_engineering':0},
            'major_scores': None,
            'current_major': None,
            'current_mid': None, 
            'current_qid':None
        }

        self.state=sessions[session_id]
        # pick first question
        q, opts, qid, cluster = pick_question(self.clusters,self.state['cluster_scores'])
        self.state['current_cluster'] = cluster
        self.state['current_qid'] = qid

        return 'cluster', q, opts

    def answer(self, user_answer):
        qid = self.state['current_qid']
        mid = self.state['current_mid']
        major = self.state['current_major']
        cluster = self.state['current_cluster']

        if self.state['quiz_stage'] == 'cluster':
            self.state['cluster_scores'] = softmax(update_cluster_weights(self.clusters, user_answer, qid, cluster, self.state['cluster_scores']))
            if any(s >= 0.65 for s in self.state['cluster_scores'].values()):
                # move to major stage
                self.state['quiz_stage'] = 'major'
                self.state['current_cluster'] = max(self.state['cluster_scores'], key=self.state['cluster_scores'].get)
                self.state['major_scores'] = init_major_scores(self.state['current_cluster'])
                q, opts, new_mid, major = pick_major_question(self.clusters,self.state['major_scores'], self.state['current_cluster'])
                self.state['current_mid'] = new_mid
                self.state['current_major'] = major

                return 'major', q, opts
            else:
                q, opts, new_qid, cluster = pick_question(self.clusters,self.state['cluster_scores'])
                self.state['current_qid'] = new_qid
                self.state['current_cluster'] = cluster
                return 'cluster', q, opts

        elif self.state['quiz_stage'] == 'major':
            self.state['major_scores'] = softmax(update_major_weights(self.clusters,
                self.state['current_cluster'], mid, user_answer, major, self.state['major_scores']
            ))

            if any(s >= 0.65 for s in self.state['major_scores'].values()):
                self.final_major = max(self.state['major_scores'], key=self.state['major_scores'].get)
                self.done=True
                return 'done', self.final_major, None 
            else:
                q, opts, new_mid, major = pick_major_question(self.clusters,self.state['major_scores'], self.state['current_cluster'])
                self.state['current_mid'] = new_mid
                self.state['current_major'] = major
                return 'major', q, opts
