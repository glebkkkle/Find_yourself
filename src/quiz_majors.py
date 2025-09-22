from ds import STEM_data_cluster, Business_cluster, STEM_engineering_cluster, Humanities_cluster
import numpy as np 

clusters={}

clusters['STEM_data']=STEM_data_cluster
clusters['Business']=Business_cluster

clusters['Humanities']=Humanities_cluster
clusters['STEM_engineering']=STEM_engineering_cluster

def softmax(scores, temperature=1.0):

    keys = list(scores.keys()) 
    vals = np.array(list(scores.values()))
    
    exp_scores = np.exp(vals / temperature)   
    probs = exp_scores / np.sum(exp_scores)
    
    return dict(zip(keys, probs))


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

def update_cluster_weights(user_ans, cluster_id, cluster, cluster_scores):
    question = clusters[cluster]['cluster_questions'][cluster_id]
    answer_weight = question['answer_weights'][user_ans]


    for cl, base_weight in question['cluster_weights'].items():
        cluster_scores[cl] += base_weight * answer_weight

    print(cluster_scores)
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



def _format_cluster(cluster_scores):
    chosen_cluster=max(cluster_scores, key=lambda x : cluster_scores[x])    
    majors=clusters[chosen_cluster]['majors']
    
    mjs=[{'name':x['major_name'], 'description':x['major_metadata']['description']} for x in majors]

    return mjs

def func():
    threshold=0.95
    clusters_scores={'STEM_data':0, "Business":0, "Humanities":0, "STEM_engineering":0}
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









