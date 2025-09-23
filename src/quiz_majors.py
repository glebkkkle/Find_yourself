from ds import STEM_data_cluster, Business_cluster, STEM_engineering_cluster, Humanities_cluster
import numpy as np 

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

    print(dominant_cluster)
    cluster_questions_list=clusters[dominant_cluster]['cluster_questions']
    
    for question_id in range(len(cluster_questions_list)):
        
        if not cluster_questions_list[question_id]['seen']:
            answer_options=cluster_questions_list[question_id]['answer_weights'].keys()
            lst=[*answer_options]
            clusters[dominant_cluster]['cluster_questions'][question_id]['seen']=True

            return cluster_questions_list[question_id]['question_text'], lst, question_id, dominant_cluster


    return None, None, None, None


dic={'Data Science': {'majors' : {
    "Data Science": {
        "major_metadata": {
            "description": "Focuses on extracting insights from large datasets, predictive modeling, and statistical analysis.",
            "filters": ["data", "analytics", "programming", "statistics", "machine learning"]
        },
        "major_questions": [
            {
                "question_text": "Do you enjoy cleaning and preparing datasets for analysis?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.7, "Data Analytics": 0.8},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": 0.1, "No": 0.0},
                "seen": False
            },
            {
                "question_text": "Are you interested in building machine learning models to predict outcomes?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.9},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.6, "Sometimes": 0.3, "Not really": 0.1, "No": 0.0},
                "seen": False
            }
        ]
    },
    "Artificial Intelligence": {
        "major_metadata": {
            "description": "Focuses on algorithms that enable computers to learn, reason, and make decisions.",
            "filters": ["AI", "programming", "data", "machine learning", "robotics"]
        },
        "major_questions": [
            {
                "question_text": "Do you enjoy working on neural networks and deep learning?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Artificial Intelligence": 1.0, "Data Science": 0.7},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.6, "Sometimes": 0.3, "Not really": 0.1, "No": 0.0},
                "seen": False
            },
            {
                "question_text": "Do you like experimenting with AI projects like chatbots or autonomous agents?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Artificial Intelligence": 1.0},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": 0.1, "No": 0.0},
                "seen": False
            }
        ]
    },
    "Accounting": {
        "major_metadata": {
            "description": "Focuses on financial reporting, business analytics, and managing monetary data.",
            "filters": ["data", "numbers", "business", "finance"]
        },
        "major_questions": [
            {
                "question_text": "Do you enjoy working with financial datasets and ledgers?",
                "cluster_weights": {"STEM_data": 0.8},
                "major_weights": {"Accounting": 1.0},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": 0.1, "No": 0.0},
                "seen": False
            },
            {
                "question_text": "Are you comfortable preparing reports and analyzing business metrics?",
                "cluster_weights": {"STEM_data": 0.8},
                "major_weights": {"Accounting": 1.0},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.6, "Sometimes": 0.3, "Not really": 0.1, "No": 0.0},
                "seen": False
            }
        ]
    },
    "Data Analytics": {
        "major_metadata": {
            "description": "Focuses on analyzing business and operational data to provide actionable insights.",
            "filters": ["data", "statistics", "business intelligence", "visualization"]
        },
        "major_questions": [
            {
                "question_text": "Do you enjoy building dashboards and visualizing data trends?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Analytics": 1.0, "Data Science": 0.7},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": 0.1, "No": 0.0},
                "seen": False
            },
            {
                "question_text": "Are you interested in making business decisions based on data insights?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Analytics": 1.0, "Accounting": 0.5},
                "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": 0.1, "No": 0.0},
                "seen": False
            }
        ]
    }
}}
}


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


def update_major_weights( cluster, major_id,user_ans,  major_name, major_scores):
    question=clusters[cluster]['majors'][major_name]['major_questions'][major_id]
    answer_weight=question['answer_weights'][user_ans]

    for mj, base_weight in question['major_weights'].items():
        major_scores[mj]+=base_weight * answer_weight

    return major_scores




def _format_cluster(cluster_scores):
    chosen_cluster=max(cluster_scores, key=lambda x : cluster_scores[x])    
    majors=clusters[chosen_cluster]['majors']
    
    mjs=[{'name':x['major_name'], 'description':x['major_metadata']['description']} for x in majors]

    return mjs




def run_cluster_quiz():
    threshold=0.80
    clusters_scores={'STEM_data':0, "Business":0, "Humanities":0, "STEM_engineering":0}
    while True:
        if any([clusters_scores[x] >= threshold for x in clusters_scores]):
            break

        question, opt, id, cluster_q=pick_question(clusters_scores) 
        
        if any([clusters_scores[x] > 0.55 for x in clusters_scores]):
            q=pick_major_question(clusters_scores)
            print(f'Major question:{q}')
            
        try:
            user_ans=_get_user_answer(question, opt)
        except TypeError:
            break
        clusters_scores=softmax(update_cluster_weights(user_ans, id, cluster_q, clusters_scores))

        
    cluster=_format_cluster(clusters_scores)

    return cluster



major_scores={'STEM_data': {'Data Science':0, 'Artificial Intelligence':0, 'Accounting':0, 'Data Analytics':0 }, 
                'Business':{"Business Administration":0, 'Economics':0,  'Finance':0, 'Management':0 },
                'Humanities':{'History':0, 'Philosophy':0, 'Linguistics':0,'International Relations':0 },
                'STEM_engineering':{'Mechanical Engineering':0,'Electrical Engineering':0, 'Civil Engineering':0, 'Biomedical Engineering':0 }}

def run_major_quiz(cluster):
    majors=major_scores[cluster]
    threhold=0.7

    while True:
        print(majors)
        if any([majors[x] >=threhold for x in majors]):
            
            break
        question, options, major_id, major_name=pick_major_question(majors, cluster)
        
        try:
            _get_user_answer(question, options)
        except TypeError:
            break
        majors=softmax(update_major_weights(cluster, major_id, 'Yes', major_name, majors))
    
    return

run_major_quiz('STEM_data')


major_scores={'STEM_data': {'Data Science':0, 'Artificial Intelligence':0, 'Accounting':0, 'Data Analytics':0 }, 
                'Business':{"Business Administration":0, 'Economics':0,  'Finance':0, 'Management':0 },
                'Humanities':{'History':0, 'Philosophy':0, 'Linguistics':0,'International Relations':0 },
                'STEM_engineering':{'Mechanical Engineering':0,'Electrical Engineering':0, 'Civil Engineering':0, 'Biomedical Engineering':0 }}

(pick_major_question(major_scores['STEM_data'], 'STEM_data'))
(update_major_weights('STEM_data', 0, 'Yes', 'Data Science', major_scores['STEM_data']))

def run_quiz():
    

    return 