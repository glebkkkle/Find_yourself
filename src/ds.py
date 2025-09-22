STEM_data_cluster = {
    "cluster_name": "STEM_data",
    "cluster_metadata": {
        "filters": ["math", "analytics", "data", "programming", "problem-solving"],
        "description": "Majors focused on quantitative analysis, computational thinking, and data-driven problem solving."
    },
    "cluster_questions": [
        {
            "question_text": "Do you like working with data?",
            "cluster_weights": { 
                "STEM_data": 1.0,
                "STEM_engineering": 0.6,
                "Humanities": 0.1,
                "Business": 0.5
            },
            "major_weights": { 
                "Data Science": 1.0,
                "Artificial Intelligence": 0.8,
                "Accounting": 0.7,
                "Data Analytics": 1.0
            },
            "answer_weights": {  
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -0.5,
                "No": -1
            
            },
             
            "question_text": "Do you enjoy working with large datasets to uncover hidden trends?",
            "cluster_weights": {"STEM_data": 1.0, "Business": 0.4, "STEM_engineering": 0.3, "Humanities": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},
  
            "question_text": "Would you find it rewarding to build predictive models for real-world problems?",
            "cluster_weights": {"STEM_data": 1.0, "Business": 0.5, "STEM_engineering": 0.4, "Humanities": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},


            "question_text": "Do you like exploring statistical tools and programming languages like Python or R?",
            "cluster_weights": {"STEM_data": 1.0, "STEM_engineering": 0.5, "Business": 0.3, "Humanities": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},


            'seen':True
            },
        {
            "question_text": "I can see myself working on prediction algorithms.",
            "cluster_weights": {
                "STEM_data": 1.0,
                "STEM_engineering": 0.4,
                "Humanities": 0.0,
                "Business": 0.3
            },
            "major_weights": {
                "Data Science": 1.0,
                "Artificial Intelligence": 1.0,
                "Accounting": 0.2,
                "Data Analytics": 0.8
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.6,
                "Sometimes": 0.3,
                "Not really": -0.5,
                "No": -1
            },
            'seen':False
        },
        {
            "question_text": "Do you enjoy programming or writing scripts to automate tasks?",
            "cluster_weights": {
                "STEM_data": 1.0,
                "STEM_engineering": 0.7,
                "Humanities": 0.0,
                "Business": 0.3
            },
            "major_weights": {
                "Data Science": 0.8,
                "Artificial Intelligence": 1.0,
                "Accounting": 0.2,
                "Data Analytics": 0.7
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.6,
                "Sometimes": 0.3,
                "Not really": -.5,
                "No": -1
            }, 
            'seen':False
        }
    ],
    "majors": [
        {
            "major_name": "Data Science",
            "major_metadata": {
                "description": "Focuses on extracting insights from large datasets, predictive modeling, and statistical analysis.",
                "filters": ["data", "analytics", "programming", "statistics", "machine learning"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy cleaning and preparing datasets for analysis?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.7, "Data Analytics": 0.8},
                    "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":0.1, "No":0.0}
                },
                {
                    "question_text": "Are you interested in building machine learning models to predict outcomes?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.9},
                    "answer_weights": {"Yes":1.0, "Mostly":0.6, "Sometimes":0.3, "Not really":0.1, "No":0.0}
                }
            ]
        },
        {
            "major_name": "Artificial Intelligence",
            "major_metadata": {
                "description": "Focuses on algorithms that enable computers to learn, reason, and make decisions.",
                "filters": ["AI", "programming", "data", "machine learning", "robotics"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working on neural networks and deep learning?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Artificial Intelligence": 1.0, "Data Science": 0.7},
                    "answer_weights": {"Yes":1.0, "Mostly":0.6, "Sometimes":0.3, "Not really":0.1, "No":0.0}
                },
                {
                    "question_text": "Do you like experimenting with AI projects like chatbots or autonomous agents?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Artificial Intelligence": 1.0},
                    "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":0.1, "No":0.0}
                }
            ]
        },
        {
            "major_name": "Accounting",
            "major_metadata": {
                "description": "Focuses on financial reporting, business analytics, and managing monetary data.",
                "filters": ["data", "numbers", "business", "finance"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working with financial datasets and ledgers?",
                    "cluster_weights": {"STEM_data": 0.8},
                    "major_weights": {"Accounting": 1.0},
                    "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":0.1, "No":0.0}
                },
                {
                    "question_text": "Are you comfortable preparing reports and analyzing business metrics?",
                    "cluster_weights": {"STEM_data": 0.8},
                    "major_weights": {"Accounting": 1.0},
                    "answer_weights": {"Yes":1.0, "Mostly":0.6, "Sometimes":0.3, "Not really":0.1, "No":0.0}
                }
            ]
        },
        {
            "major_name": "Data Analytics",
            "major_metadata": {
                "description": "Focuses on analyzing business and operational data to provide actionable insights.",
                "filters": ["data", "statistics", "business intelligence", "visualization"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy building dashboards and visualizing data trends?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Analytics": 1.0, "Data Science": 0.7},
                    "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":0.1, "No":0.0}
                },
                {
                    "question_text": "Are you interested in making business decisions based on data insights?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Analytics": 1.0, "Accounting": 0.5},
                    "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":0.1, "No":0.0}
                }
            ]
        }
    ]
}


Business_cluster = {
    "cluster_name": "Business",
    "cluster_metadata": {
        "filters": ["finance", "management", "markets", "communication", "leadership"],
        "description": "Majors focused on business operations, financial systems, leadership, and organizational strategy."
    },
    "cluster_questions": [
        {
            "question_text": "Do you enjoy analyzing markets and financial trends?",
            "cluster_weights": {
                "Business": 1.0,
                "STEM_data": 0.6,
                "Humanities": 0.2,
                "STEM_engineering": 0.2
            },
            "major_weights": {
                "Economics": 1.0,
                "Accounting": 0.8,
                "Business Administration": 1.0,
                "Finance": 1.0
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really":-.5,
                "No":-1
            },
            "seen": False
        },
        {
            "question_text": "Do you enjoy leading people and managing teams?",
            "cluster_weights": {
                "Business": 1.0,
                "Humanities": 0.4,
                "STEM_data": 0.3,
                "STEM_engineering": 0.3
            },
            "major_weights": {
                "Business Administration": 1.0,
                "Management": 1.0,
                "Economics": 0.3,
                "Finance": 0.5
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": 0.1,
                "No": 0.0
            }, 
            "seen": False
        },
        {
            "question_text": "Do you enjoy creating strategies to improve organizations?",
            "cluster_weights": {
                "Business": 1.0,
                "Humanities": 0.3,
                "STEM_engineering": 0.3,
                "STEM_data": 0.4
            },
            "major_weights": {
                "Business Administration": 1.0,
                "Management": 1.0,
                "Economics": 0.5,
                "Finance": 0.4
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.6,
                "Sometimes": 0.3,
                "Not really": -.5,
                "No": -1
            }, 
             "question_text": "Do you enjoy thinking about strategies for growing organizations?",
            "cluster_weights": {"Business": 1.0, "STEM_data": 0.4, "Humanities": 0.3, "STEM_engineering": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6}, 

                "question_text": "Would you like to manage teams or lead projects in a company setting?",
    "cluster_weights": {"Business": 1.0, "STEM_data": 0.3, "Humanities": 0.3, "STEM_engineering": 0.2},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6} ,

    "question_text": "Do you find decision-making about resources and investments interesting?",
    "cluster_weights": {"Business": 1.0, "STEM_data": 0.5, "Humanities": 0.2, "STEM_engineering": 0.2},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6}, 

            "seen": False
        }
    ],
    "majors": [
        {
            "major_name": "Business Administration",
            "major_metadata": {
                "description": "Focuses on managing organizations, leadership, operations, and decision-making in business contexts.",
                "filters": ["management", "leadership", "strategy", "operations", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy organizing processes and optimizing efficiency?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Business Administration": 1.0, "Management": 0.9},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Are you comfortable making big decisions that affect a group or company?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Business Administration": 1.0, "Management": 0.8},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Economics",
            "major_metadata": {
                "description": "Focuses on market behavior, economic theory, and data-driven decision-making in societies and businesses.",
                "filters": ["economics", "markets", "policy", "analysis", "data"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy studying how supply and demand affect prices?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0, "Finance": 0.8},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to research economic policies and their social impacts?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0, "Political Science": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Finance",
            "major_metadata": {
                "description": "Focuses on investment, corporate finance, and financial markets to optimize resource allocation.",
                "filters": ["finance", "markets", "investment", "risk analysis", "data"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy analyzing investment risks and returns?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0, "Economics": 0.6, "Accounting": 0.8},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to manage portfolios or corporate budgets?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0, "Accounting": 0.7},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Management",
            "major_metadata": {
                "description": "Focuses on leadership, organizational behavior, and decision-making in teams and companies.",
                "filters": ["leadership", "management", "organization", "strategy", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy motivating others and resolving conflicts in groups?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Management": 1.0, "Business Administration": 0.8},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to focus on improving teamwork and collaboration in organizations?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Management": 1.0, "Business Administration": 0.8},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        }
    ]
}

Humanities_cluster = {
    "cluster_name": "Humanities",
    "cluster_metadata": {
        "filters": ["history", "languages", "culture", "philosophy", "writing", "communication"],
        "description": "Majors focused on human culture, language, history, philosophy, and creative expression."
    },
    "cluster_questions": [
        {
            "question_text": "Do you enjoy studying history, culture, or society?",
            "cluster_weights": {
                "Humanities": 1.0,
                "Business": 0.3,
                "STEM_data": 0.2,
                "STEM_engineering": 0.1
            },
            "major_weights": {
                "History": 1.0,
                "Philosophy": 0.5,
                "Linguistics": 0.6,
                "International Relations": 0.7
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -0.5,
                "No": -1
            },
            "seen": False
        },
        {
            "question_text": "Do you enjoy writing, interpreting texts, or expressing ideas?",
            "cluster_weights": {
                "Humanities": 1.0,
                "Business": 0.4,
                "STEM_data": 0.1,
                "STEM_engineering": 0.0
            },
            "major_weights": {
                "Philosophy": 0.8,
                "History": 0.6,
                "Linguistics": 0.8,
                "International Relations": 0.5
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -.5,
                "No": -1
            },
            "question_text": "Do you enjoy exploring history, culture, or philosophy to understand people better?",
            "cluster_weights": {"Humanities": 1.0, "Business": 0.4, "STEM_data": 0.3, "STEM_engineering": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6}, 
            "question_text": "Would you like to work in a field focused on communication and critical thinking?",
            "cluster_weights": {"Humanities": 1.0, "Business": 0.3, "STEM_data": 0.3, "STEM_engineering": 0.2},
            "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6}, 


     "question_text": "Do you enjoy writing, discussing ideas, or analyzing human behavior?",
    "cluster_weights": {"Humanities": 1.0, "Business": 0.5, "STEM_data": 0.3, "STEM_engineering": 0.2},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6}, 
            "seen": False
        },
        {
            "question_text": "Do you enjoy analyzing how people communicate and use language?",
            "cluster_weights": {
                "Humanities": 1.0,
                "Business": 0.3,
                "STEM_data": 0.2,
                "STEM_engineering": 0.1
            },
            "major_weights": {
                "Linguistics": 1.0,
                "Philosophy": 0.5,
                "International Relations": 0.7,
                "History": 0.5
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -.5,
                "No": -1
            },
            "seen": False
        }
    ],
    "majors": [
        {
            "major_name": "History",
            "major_metadata": {
                "description": "Focuses on understanding past events, civilizations, and their impact on society.",
                "filters": ["history", "culture", "society", "writing", "analysis"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy studying different historical periods and civilizations?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"History": 1.0, "International Relations": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to research how the past influences current society?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"History": 1.0, "Philosophy": 0.5},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Philosophy",
            "major_metadata": {
                "description": "Focuses on critical thinking, ethics, reasoning, and the study of knowledge and existence.",
                "filters": ["philosophy", "logic", "ethics", "writing", "critical thinking"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy discussing abstract ideas such as truth, justice, or morality?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "History": 0.4},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Do you enjoy analyzing arguments and improving logical reasoning?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "Linguistics": 0.5},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Linguistics",
            "major_metadata": {
                "description": "Focuses on the scientific study of language, its structure, and its role in communication.",
                "filters": ["linguistics", "language", "communication", "analysis", "culture"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy studying grammar, syntax, or the structure of languages?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Linguistics": 1.0, "Philosophy": 0.4},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to explore how language shapes culture and society?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Linguistics": 1.0, "International Relations": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "International Relations",
            "major_metadata": {
                "description": "Focuses on global politics, diplomacy, and how nations interact with each other.",
                "filters": ["international relations", "politics", "diplomacy", "culture", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy learning about diplomacy and how countries interact?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "History": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to work with international organizations and policies?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "Political Science": 0.7},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        }
    ]
}


STEM_engineering_cluster = {
    "cluster_name": "STEM_engineering",
    "cluster_metadata": {
        "filters": ["design", "problem-solving", "physics", "engineering", "innovation"],
        "description": "Majors focused on designing, building, and optimizing systems, machines, and infrastructure."
    },
    "cluster_questions": [
        {
            "question_text": "Do you enjoy designing and building physical systems or structures?",
            "cluster_weights": {
                "STEM_engineering": 1.0,
                "STEM_data": 0.4,
                "Business": 0.2,
                "Humanities": 0.1
            },
            "major_weights": {
                "Mechanical Engineering": 1.0,
                "Civil Engineering": 1.0,
                "Electrical Engineering": 0.6,
                "Biomedical Engineering": 0.6
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -.5,
                "No": -1
            },
            "seen": False
        },
        {
            "question_text": "Do you enjoy applying physics and math to solve real-world problems?",
            "cluster_weights": {
                "STEM_engineering": 1.0,
                "STEM_data": 0.6,
                "Business": 0.2,
                "Humanities": 0.0
            },
            "major_weights": {
                "Mechanical Engineering": 1.0,
                "Electrical Engineering": 1.0,
                "Civil Engineering": 0.8,
                "Biomedical Engineering": 0.7
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -.5,
                "No": -1
            },
            "seen": False
        },
        {
            "question_text": "Do you enjoy working on technologies that improve human life (like medical devices or clean energy)?",
            "cluster_weights": {
                "STEM_engineering": 1.0,
                "STEM_data": 0.5,
                "Business": 0.3,
                "Humanities": 0.2
            },
            "major_weights": {
                "Biomedical Engineering": 1.0,
                "Mechanical Engineering": 0.7,
                "Electrical Engineering": 0.8,
                "Civil Engineering": 0.6
            },
            "answer_weights": {
                "Yes": 1.0,
                "Mostly": 0.7,
                "Sometimes": 0.4,
                "Not really": -.5,
                "No": -1
            },
    "question_text": "Do you enjoy solving real-world problems by designing technical systems?",
    "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.4, "Business": 0.3, "Humanities": 0.1},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},

    "question_text": "Would you like to work on improving machines, structures, or processes?",
    "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.3, "Business": 0.3, "Humanities": 0.1},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},

     "question_text": "Do you see yourself applying physics and math concepts to engineering challenges?",
    "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.5, "Business": 0.2, "Humanities": 0.1},
    "answer_weights": {"Yes": 1.0, "Mostly": 0.7, "Sometimes": 0.4, "Not really": -0.3, "No": -0.6},



            "seen": False
        }
    ],
    "majors": [
        {
            "major_name": "Mechanical Engineering",
            "major_metadata": {
                "description": "Focuses on designing and optimizing machines, vehicles, and mechanical systems.",
                "filters": ["mechanical", "design", "physics", "energy", "manufacturing"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working with engines, machines, or robotics?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Electrical Engineering": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to design and test new mechanical devices?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Biomedical Engineering": 0.5},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Electrical Engineering",
            "major_metadata": {
                "description": "Focuses on circuits, electronics, power systems, and communication technologies.",
                "filters": ["electrical", "circuits", "electronics", "signal processing", "energy"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working with electronics, circuits, or power systems?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Mechanical Engineering": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to work on renewable energy or communication technologies?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Civil Engineering": 0.4},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Civil Engineering",
            "major_metadata": {
                "description": "Focuses on designing and constructing infrastructure such as bridges, roads, and buildings.",
                "filters": ["civil", "infrastructure", "design", "construction", "environment"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working on construction projects or infrastructure design?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0, "Mechanical Engineering": 0.5},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to improve urban planning or environmental sustainability through engineering?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0, "Environmental Science": 0.7},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        },
        {
            "major_name": "Biomedical Engineering",
            "major_metadata": {
                "description": "Focuses on applying engineering to healthcare, including medical devices and biotechnology.",
                "filters": ["biomedical", "healthcare", "devices", "bioengineering", "innovation"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy combining biology and engineering to solve medical problems?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Biomedical Engineering": 1.0, "Data Science": 0.5},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                },
                {
                    "question_text": "Would you like to design medical devices or prosthetics?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Biomedical Engineering": 1.0, "Mechanical Engineering": 0.6},
                    "answer_weights": {"Yes":1.0,"Mostly":0.7,"Sometimes":0.4,"Not really":0.1,"No":0.0}
                }
            ]
        }
    ]
}
