from ds import STEM_data_cluster, Business_cluster, STEM_engineering_cluster, Humanities_cluster
import numpy as np 
import requests


clusters={}

clusters['STEM_data']=STEM_data_cluster
clusters['Business']=Business_cluster

clusters['Humanities']=Humanities_cluster
clusters['STEM_engineering']=STEM_engineering_cluster

def softmax(scores, temperature=0.5):
    keys = list(scores.keys()) 
    vals = np.array(list(scores.values()))
    
    exp_scores = np.exp(vals / temperature)   
    probs = exp_scores / np.sum(exp_scores)
    
    return dict(zip(keys, probs))

#pick cluster question
def pick_question(cluster_scores, alpha=None):
    dominant_cluster = max(cluster_scores, key=lambda x : cluster_scores[x])

    cluster_questions_list=clusters[dominant_cluster]['cluster_questions']
    
    for question_id in range(len(cluster_questions_list)):
        
        if not cluster_questions_list[question_id]['seen']:
            answer_options=cluster_questions_list[question_id]['answer_weights'].keys()
            lst=[*answer_options]
            clusters[dominant_cluster]['cluster_questions'][question_id]['seen']=True

            return cluster_questions_list[question_id]['question_text'], lst, question_id, dominant_cluster


    return None, None, None, None

#pick major question
def pick_major_question(major_scores, cluster):
    dominant_major = max(major_scores, key=lambda x : major_scores[x])
    q_lst=clusters[cluster]['majors'][dominant_major]['major_questions']


    for major_id in range(len(q_lst)):

        if not q_lst[major_id]['seen']:
            clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['seen']=True
            q=clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['question_text']
            options=clusters[cluster]['majors'][dominant_major]['major_questions'][major_id]['answer_weights']
            
            return q, options, major_id, dominant_major
        
    return None, None, None, None

    
def update_cluster_weights(user_ans, cluster_id, cluster, cluster_scores, major_id=None):
    question = clusters[cluster]['cluster_questions'][cluster_id]
    answer_weight = question['answer_weights'][user_ans]

    for cl, base_weight in question['cluster_weights'].items():
        cluster_scores[cl] += base_weight * answer_weight

    return cluster_scores


def _get_user_answer(q, options):
    print('----------------------------')
    print(q)
    print('----------------------------')
    

    for option in options:
        print(option)
    print(' ')

    user_input=input('Select one Option:')
    while user_input not in options:
        user_input=input('Select one Option:')

    return user_input



def update_major_weights(cluster, major_id,user_ans,  major_name, major_scores):
    question=clusters[cluster]['majors'][major_name]['major_questions'][major_id]
    answer_weight=question['answer_weights'][user_ans]

    for mj, base_weight in question['major_weights'].items():
        major_scores[mj]+=base_weight * answer_weight

    return major_scores




def _format_cluster(cluster_scores):
    chosen_cluster=max(cluster_scores, key=lambda x : cluster_scores[x])    
    return chosen_cluster

get_user_response_url=''

def run_cluster_quiz(cluster_scores):
    threshold=0.80
    while True:
        if any([clusters_scores[x] >= threshold for x in clusters_scores]):
            break
        question, opt, id, cluster_q=pick_question(clusters_scores) 
        try:
            user_ans=_get_user_answer(question, opt)
        except TypeError:
            break
        clusters_scores=softmax(update_cluster_weights(user_ans, id, cluster_q, clusters_scores))


    cluster=_format_cluster(clusters_scores)


    return cluster

quiz_states={'quiz_state':'abc123', 'cluster_scores':[], 'major_scores':[], 'done':False}

def run_cl_quiz(session_id):
    if quiz_states['done']==True:
        return 'Over'

    threshold=0.8
    cluster_scores=quiz_states[session_id]

    if any([cluster_scores[x] >=threshold for x in cluster_scores]):
        quiz_states['done']=True
        return max(cluster_scores, key=lambda x : cluster_scores[x])
    
    question, opt, id, cluster_q=pick_question(cluster_scores)
    payload={'q':question, 'o':opt}

    response=requests.post(get_user_response_url, json=payload)

    return 


def run_major_quiz(cluster):
    major_scores={'STEM_data': {'Data Science':0, 'Artificial Intelligence':0, 'Accounting':0, 'Data Analytics':0 }, 
                'Business':{"Business Administration":0, 'Economics':0,  'Finance':0, 'Management':0 },
                'Humanities':{'History':0, 'Philosophy':0, 'Linguistics':0,'International Relations':0 },
                'STEM_engineering':{'Mechanical Engineering':0,'Electrical Engineering':0, 'Civil Engineering':0, 'Biomedical Engineering':0 }}
    majors=major_scores[cluster]
    threhold=0.8

    while True:
        if any([majors[x] >=threhold for x in majors]):
            break
        question, options, major_id, major_name=pick_major_question(majors, cluster)
        
        try:
            user_ans=_get_user_answer(question, options)
        except TypeError:
            break
        majors=softmax(update_major_weights(cluster, major_id, user_ans, major_name, majors))

    return max(majors, key=lambda x : majors[x])


def run_quiz(cluster_scores, major_scores):
    chosen_cluster=run_cluster_quiz(cluster_scores)

    print('-------------------------------')
    print('-------------------------------')
    
    major=run_major_quiz(chosen_cluster)

    return major

dic={'user_id':'abc123'}



def _identify_session(payload, states):
    session_id=payload['user_id']

    cluster_scores=states['cluster_scores']
    major_scores=states['major_scores']


    return 

def init_major_scores(cluster):
    major_scores = {
        'STEM_data': {'Data Science': 0, 'Artificial Intelligence': 0, 'Accounting': 0, 'Data Analytics': 0},
        'Business': {'Business Administration': 0, 'Economics': 0, 'Finance': 0, 'Management': 0},
        'Humanities': {'History': 0, 'Philosophy': 0, 'Linguistics': 0, 'International Relations': 0},
        'STEM_engineering': {'Mechanical Engineering': 0, 'Electrical Engineering': 0, 'Civil Engineering': 0, 'Biomedical Engineering': 0}
    }
    return major_scores[cluster].copy() 



user_sessions = {
    'user_id':
    "user123",
    "cluster_quiz": {
            "scores": {...},
            "current_question": None,
            "finished": False
        },
        "major_quiz": {
            "scores": {...},
            "current_question": None,
            "finished": False
        }
    }



