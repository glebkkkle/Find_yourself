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
                "STEM_data": .9,
                "STEM_engineering": 0.5,
                "Humanities": 0.1,
                "Business": 0.4
            },
            "major_weights": { 
                "Data Science": 1.0,
                "Artificial Intelligence": 0.8,
                "Accounting": 0.7,
                "Data Analytics": 1.0
            },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        }, 
        {
            "question_text": "Do you enjoy solving problems using mathematical or statistical methods?",
            "cluster_weights": {"STEM_data": 1.0, "STEM_engineering": 0.6, "Business": 0.4, "Humanities": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },

        {
            "question_text": "Would you like to work with machine learning or AI systems in the future?",
            "cluster_weights": {"STEM_data": 1.0, "STEM_engineering": 0.5, "Business": 0.3, "Humanities": 0.1},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },

        {   "question_text": "Do you enjoy creating visualizations to explain data and insights?",
            "cluster_weights": {"STEM_data": 1.0, "Business": 0.6, "STEM_engineering": 0.3, "Humanities": 0.4},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },

        {   "question_text": "Do you enjoy working with large datasets to uncover hidden trends?",
            "cluster_weights": {"STEM_data": 1.0, "Business": 0.4, "STEM_engineering": 0.3, "Humanities": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },


        {   "question_text": "Would you find it rewarding to build predictive models for real-world problems?",
            "cluster_weights": {"STEM_data": 1.0, "Business": 0.5, "STEM_engineering": 0.4, "Humanities": 0.2},

    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },

        {   "question_text": "Do you like exploring statistical tools and programming languages like Python or R?",
            "cluster_weights": {"STEM_data": 1.0, "STEM_engineering": 0.5, "Business": 0.3, "Humanities": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        }
    ],
   
    'majors' : {
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
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                },
                {
                    "question_text": "Are you interested in building machine learning models to predict outcomes?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.9},
                    "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                }, 
                {
                "question_text": "Do you enjoy working with programming languages like Python or R for data tasks?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.6, "Data Analytics": 0.7},
                "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.1, "No": -.2},
                "seen": False
            },
            {
                "question_text": "Do you like exploring large datasets to find meaningful insights?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0, "Data Analytics": 0.9},
                "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.1, "No": -.2},
                "seen": False
            }, 
            {
            "question_text": "Do you enjoy testing and improving models using metrics and validation techniques?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Science": 1.0, "Artificial Intelligence": 0.8},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
            "seen": False
            }, 
            {
                "question_text": "Would you like to work with real-world messy data (e.g., social media, sensor data, business data)?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0},
                "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
                "seen": False
            },
            {
                "question_text": "Do you enjoy creating data visualizations to communicate findings?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Data Science": 1.0, "Data Analytics": 1.0},
                "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.4, "Not really": -0.1, "No": -0.3},
                "seen": False
            },
                    {
            "question_text": "Are you interested in learning statistical methods to analyze and interpret data?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Science": 1.0, "Data Analytics": 0.8},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
            "seen": False
        },
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
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                },
                {
                    "question_text": "Do you like experimenting with AI projects like chatbots or autonomous agents?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Artificial Intelligence": 1.0},
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                }, 
                {
                "question_text": "Are you fascinated by the idea of machines making intelligent decisions?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Artificial Intelligence": 1.0, "Data Science": 0.6},
                "answer_weights": {"Yes":1.0, "Mostly":0.6, "Sometimes":0.3, "Not really":-0.1, "No":-0.2},
                "seen": False
                },
                {
                "question_text": "Do you want to work on computer vision or natural language processing projects?",
                "cluster_weights": {"STEM_data": 1.0},
                "major_weights": {"Artificial Intelligence": 1.0, "Data Science": 0.7},
                "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":-0.1, "No":-0.2},
                "seen": False
                }, 
                        {
            "question_text": "Are you interested in applications like computer vision, natural language processing, or robotics?",
            "cluster_weights": {"STEM_AI": 1.0},
            "major_weights": {"Artificial Intelligence": 1.0},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.4, "Not really": -0.2, "No": -0.4},
            "seen": False
        }, 
                {
            "question_text": "Would you enjoy designing algorithms that allow machines to make decisions or predictions?",
            "cluster_weights": {"STEM_AI": 1.0},
            "major_weights": {"Artificial Intelligence": 1.0},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
            "seen": False
        },
                {
            "question_text": "Do you find the idea of teaching machines to mimic human intelligence exciting?",
            "cluster_weights": {"STEM_AI": 1.0},
            "major_weights": {"Artificial Intelligence": 1.0},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.4, "Not really": -0.2, "No": -0.5},
            "seen": False
        },
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
                    "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                },
                {
                    "question_text": "Are you comfortable preparing reports and analyzing business metrics?",
                    "cluster_weights": {"STEM_data": 0.8},
                    "major_weights": {"Accounting": 1.0},
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                }, 
                {
                "question_text": "Do you find financial problem-solving and auditing interesting?",
                "cluster_weights": {"STEM_data": 0.8, "Business": 0.5},
                "major_weights": {"Accounting": 1.0, "Data Analytics": 0.5},
                "answer_weights": {"Yes":1.0, "Mostly":0.6, "Sometimes":0.3, "Not really":-0.1, "No":-0.2},
                "seen": False
                },
                {
                "question_text": "Would you enjoy ensuring accuracy in financial statements?",
                "cluster_weights": {"STEM_data": 0.8, "Business": 0.6},
                "major_weights": {"Accounting": 1.0},
                "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":-0.1, "No":-0.2},
                "seen": False
                }   , 
                        {
            "question_text": "Do you enjoy working with numbers and ensuring financial records are accurate?",
            "cluster_weights": {"Business": 1.0},
            "major_weights": {"Accounting": 1.0, "Finance": 0.6},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.4, "Not really": -0.2, "No": -0.5},
            "seen": False
                },
            {"question_text": "Would you like analyzing budgets, expenses, and revenues to help organizations make better decisions?",
            "cluster_weights": {"Business": 1.0},
            "major_weights": {"Accounting": 1.0, "Business Administration": 0.5},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
            "seen": False
        },
                {
            "question_text": "Are you interested in learning about auditing and making sure companies follow financial regulations?",
            "cluster_weights": {"Business": 1.0},
            "major_weights": {"Accounting": 1.0},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.3, "Not really": -0.2, "No": -0.5},
            "seen": False
        },
                {
            "question_text": "Do you like working with spreadsheets, reports, and tools to track financial performance?",
            "cluster_weights": {"Business": 1.0},
            "major_weights": {"Accounting": 1.0, "Finance": 0.7},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -0.5},
            "seen": False
        }
        
            ]
        },
        "Data Analytics": {
            "major_metadata": {
                "description": "Data Analytics is designed for individuals with a strong analytical mindset and a passion for uncovering insights from complex data. Ideal candidates are naturally curious, detail-oriented, and enjoy solving problems through quantitative reasoning, allowing them to thrive in a discipline that blends technical expertise with strategic thinking. Students in this major gain foundational knowledge in statistics, data visualization, and programming languages (such as Python, R, and SQL), alongside skills in data manipulation, predictive modeling, and business intelligence tools. The program emphasizes critical soft skills, including effective communication, collaboration, and adaptability, enabling students to present data-driven insights to diverse audiences and work successfully in team-oriented environments. Graduates develop the ability to think strategically and ethically about data, ensuring their analyses drive meaningful business decisions while considering broader societal implications. Students engage in hands-on projects that mirror real-world applications, learning to collect, clean, and interpret large datasets, identify trends, and develop actionable insights that improve organizational performance. Practical experience with statistical analysis, machine learning techniques, and visualization tools prepares them to apply their knowledge across industries—from marketing and operations to finance and policy-making. Graduates of Data Analytics are well-equipped to bridge the gap between raw data and actionable insight. They can translate complex datasets into clear recommendations, optimize business processes, and contribute to data-driven innovation, emerging as analytical leaders ready to make a meaningful impact in an increasingly data-centric world.",
                "filters": ["data", "statistics", "business intelligence", "visualization"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy building dashboards and visualizing data trends?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Analytics": 1.0, "Data Science": 0.7},
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -.5},
                    "seen": False
                },
                {
                    "question_text": "Are you interested in making business decisions based on data insights?",
                    "cluster_weights": {"STEM_data": 1.0},
                    "major_weights": {"Data Analytics": 1.0, "Accounting": 0.5},
                    "answer_weights": {"Yes": .8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -0.5},
                    "seen": False
                }, 
                {
                "question_text": "Do you like finding patterns in business data to improve efficiency?",
                "cluster_weights": {"STEM_data": 1.0, "Business": 0.6},
                "major_weights": {"Data Analytics": 1.0, "Accounting": 0.5},
                "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":-0.1, "No":-0.2},
                "seen": False
            },
            {
                "question_text": "Do you enjoy translating data into insights that managers can use?",
                "cluster_weights": {"STEM_data": 1.0, "Business": 0.5},
                "major_weights": {"Data Analytics": 1.0},
                "answer_weights": {"Yes":1.0, "Mostly":0.7, "Sometimes":0.4, "Not really":-0.1, "No":-0.2},
                "seen": False
            }, 
                    {
            "question_text": "Do you enjoy examining data trends to help businesses make informed decisions?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Analytics": 1.0, "Data Science": 0.8},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.4, "Not really": -0.2, "No": -0.5},
            "seen": False
        },
                {
            "question_text": "Would you like creating dashboards and reports to visualize key performance indicators?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Analytics": 1.0, "Business Administration": 0.5},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.2, "No": -0.4},
            "seen": False
        },
                {
            "question_text": "Are you interested in using tools like SQL, Excel, or Tableau to analyze business data?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Analytics": 1.0, "Data Science": 0.6},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.6, "Sometimes": 0.3, "Not really": -0.2, "No": -0.5},
            "seen": False
        },
                {
            "question_text": "Do you like identifying patterns and insights in data to improve strategies or operations?",
            "cluster_weights": {"STEM_data": 1.0},
            "major_weights": {"Data Analytics": 1.0, "Data Science": 0.7},
            "answer_weights": {"Yes": 0.8, "Mostly": 0.5, "Sometimes": 0.3, "Not really": -0.3, "No": -0.5},
            "seen": False
        }
            ]
        }
    }}



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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },
        {
            "question_text": "Do you enjoy thinking about strategies for growing organizations?",
            "cluster_weights": {"Business": 1.0,
                                 "STEM_data": 0.4,
                                   "Humanities": 0.3, 
                                   "STEM_engineering": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False

        },
             
        {"question_text": "Would you like to manage teams or lead projects in a company setting?",
                        "cluster_weights": {"Business": 1.0,
                         "STEM_data": 0.3, 
                         "Humanities": 0.3,
                           "STEM_engineering": 0.2},

    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
                
                'seen':False
        },


        {    "question_text": "Do you find decision-making about resources and investments interesting?",
    "cluster_weights": {"Business": 1.0,
                         "STEM_data": 0.5, 
                         "Humanities": 0.2,
                         "STEM_engineering": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            "seen": False
        
        }, 
        {
    "question_text": "Do you enjoy negotiating and persuading others in discussions or deals?",
    "cluster_weights": {
        "Business": 1.0,
        "Humanities": 0.5,
        "STEM_data": 0.2,
        "STEM_engineering": 0.2
    },
    "major_weights": {
        "Business Administration": 0.9,
        "Management": 1.0,
        "Economics": 0.4,
        "Finance": 0.3
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},

{
    "question_text": "Would you enjoy working with financial statements and budgets?",
    "cluster_weights": {
        "Business": 1.0,
        "STEM_data": 0.4,
        "STEM_engineering": 0.2,
        "Humanities": 0.2
    },
    "major_weights": {
        "Accounting": 1.0,
        "Finance": 0.9,
        "Economics": 0.5,
        "Business Administration": 0.4
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},
{
    "question_text": "Do you like analyzing consumer behavior to improve marketing strategies?",
    "cluster_weights": {
        "Business": 1.0,
        "Humanities": 0.5,
        "STEM_data": 0.3,
        "STEM_engineering": 0.2
    },
    "major_weights": {
        "Business Administration": 0.8,
        "Management": 0.7,
        "Economics": 0.6,
        "Finance": 0.3
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
}
    ],
    'majors' : {
        "Business Administration": {
            "major_metadata": {
                "description": "Focuses on managing organizations, leadership, operations, and decision-making in business contexts.",
                "filters": ["management", "leadership", "strategy", "operations", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy organizing processes and optimizing efficiency?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Business Administration": 1.0, "Management": 0.9},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Are you comfortable making big decisions that affect a group or company?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Business Administration": 1.0, "Management": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Do you enjoy coordinating people and resources to achieve organizational goals?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Business Administration": 1.0, "Management": 0.9},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
            },
            {
                "question_text": "Are you interested in managing budgets and financial resources effectively?",
                "cluster_weights": {"Business": 1.0},
                "major_weights": {"Finance": 1.0, "Business Administration": 0.8, "Management": 0.7},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                "seen": False
            }

            ]
        },
        "Economics": {
            "major_metadata": {
                "description": "Focuses on market behavior, economic theory, and data-driven decision-making in societies and businesses.",
                "filters": ["economics", "markets", "policy", "analysis", "data"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy studying how supply and demand affect prices?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0, "Finance": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to research economic policies and their social impacts?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you like studying trends, markets, and the impact of policies on society?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0, "Finance": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                },
                {
                    "question_text": "Would you enjoy working with models and data to explain human behavior in markets?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Economics": 1.0},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                }
            ]
        },
        "Finance": {
            "major_metadata": {
                "description": "Focuses on investment, corporate finance, and financial markets to optimize resource allocation.",
                "filters": ["finance", "markets", "investment", "risk analysis", "data"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy analyzing investment risks and returns?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0, "Economics": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to manage portfolios or corporate budgets?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you find it exciting to analyze investments and financial risks?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0, "Economics": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                },
                {
                    "question_text": "Would you enjoy helping organizations or individuals manage their money effectively?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Finance": 1.0, "Business Administration": 0.7},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                }
            ]
        },
        "Management": {
            "major_metadata": {
                "description": "Focuses on leadership, organizational behavior, and decision-making in teams and companies.",
                "filters": ["leadership", "management", "organization", "strategy", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy motivating others and resolving conflicts in groups?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Management": 1.0, "Business Administration": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to focus on improving teamwork and collaboration in organizations?",
                    "cluster_weights": {"Business": 1.0},
                    "major_weights": {"Management": 1.0, "Business Administration": 0.8},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 

                {
                        "question_text": "Do you like motivating and guiding people toward shared goals?",
                        "cluster_weights": {"Business": 1.0},
                        "major_weights": {"Management": 1.0, "Business Administration": 0.8},
                        "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                        "seen": False
                    },
                    {
                        "question_text": "Would you enjoy taking responsibility for planning and leading a team?",
                        "cluster_weights": {"Business": 1.0},
                        "major_weights": {"Management": 1.0, "Business Administration": 0.9},
                        "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                        "seen": False
                    }
            ]
        }
    }}

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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },
        {
            "question_text": "Do you enjoy exploring history, culture, or philosophy to understand people better?",
            "cluster_weights": {"Humanities": 1.0, "Business": 0.4, "STEM_data": 0.3, "STEM_engineering": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    'seen':False
        },
        {
            "question_text": "Would you like to work in a field focused on communication and critical thinking?",
            "cluster_weights": {"Humanities": 1.0, "Business": 0.3, "STEM_data": 0.3, "STEM_engineering": 0.2},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },

    {
     "question_text": "Do you enjoy writing, discussing ideas, or analyzing human behavior?",
    "cluster_weights": {"Humanities": 1.0, "Business": 0.5, "STEM_data": 0.3, "STEM_engineering": 0.2},
    "answer_weights": {
        "Yes": 0.8,
        "Mostly": 0.5,
        "Sometimes": 0.3,
        "Not really": -0.1,
        "No": -0.2
    },
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            "seen": False
        },
        {
    "question_text": "Do you enjoy analyzing literature, art, or cultural works for deeper meaning?",
    "cluster_weights": {
        "Humanities": 1.0,
        "Business": 0.3,
        "STEM_data": 0.2,
        "STEM_engineering": 0.1
    },
    "major_weights": {
        "Literature": 1.0,
        "History": 0.4,
        "Philosophy": 0.5,
        "Linguistics": 0.6
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},

{
    "question_text": "Would you enjoy studying how different societies developed their ideas and traditions over time?",
    "cluster_weights": {
        "Humanities": 1.0,
        "Business": 0.2,
        "STEM_data": 0.2,
        "STEM_engineering": 0.1
    },
    "major_weights": {
        "History": 1.0,
        "Philosophy": 0.6,
        "Literature": 0.4,
        "Linguistics": 0.3
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},
{
    "question_text": "Do you enjoy discussing big questions about ethics, knowledge, and human existence?",
    "cluster_weights": {
        "Humanities": 1.0,
        "Business": 0.2,
        "STEM_data": 0.1,
        "STEM_engineering": 0.1
    },
    "major_weights": {
        "Philosophy": 1.0,
        "History": 0.5,
        "Literature": 0.4,
        "Linguistics": 0.3
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
}
    ],
    "majors":{
        "History":{
        "major_metadata": {
        "description": "Focuses on understanding past events, civilizations, and their impact on society.",
                "filters": ["history", "culture", "society", "writing", "analysis"]
            },
        "major_questions":[
                {
                    "question_text": "Do you enjoy studying different historical periods and civilizations?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"History": 1.0, "International Relations": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to research how the past influences current society?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"History": 1.0, "Philosophy": 0.5},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                "question_text": "Do you like analyzing primary sources such as letters, documents, or artifacts?",
                "cluster_weights": {"Humanities": 1.0},
                "major_weights": {"History": 1.0, "Philosophy": 0.5},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                "seen": False
            },
            {
                "question_text": "Would you enjoy comparing how different cultures developed over time?",
                "cluster_weights": {"Humanities": 1.0},
                "major_weights": {"History": 1.0, "International Relations": 0.7},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                "seen": False
            }
                
                ]
            
        }, 

        'Philosophy':{
            "major_metadata": {
            "description": "Focuses on critical thinking, ethics, reasoning, and the study of knowledge and existence.",
            "filters": ["philosophy", "logic", "ethics", "writing", "critical thinking"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy discussing abstract ideas such as truth, justice, or morality?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "History": 0.4},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Do you enjoy analyzing arguments and improving logical reasoning?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "Linguistics": 0.5},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you enjoy discussing big questions about existence, knowledge, or morality?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "History": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                },
                {
                    "question_text": "Would you like to evaluate different ways of reasoning and argumentation?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Philosophy": 1.0, "Linguistics": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                }
            ]
        }, 
        "Linguistics":{
            "major_metadata": {
                "description": "Focuses on the scientific study of language, its structure, and its role in communication.",
                "filters": ["linguistics", "language", "communication", "analysis", "culture"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy studying grammar, syntax, or the structure of languages?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Linguistics": 1.0, "Philosophy": 0.4},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to explore how language shapes culture and society?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"Linguistics": 1.0, "International Relations": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                "question_text": "Do you enjoy studying how languages are structured and evolve over time?",
                "cluster_weights": {"Humanities": 1.0},
                "major_weights": {"Linguistics": 1.0, "History": 0.5},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                "seen": False
            },
            {
                "question_text": "Would you like to analyze how language shapes thought and communication?",
                "cluster_weights": {"Humanities": 1.0},
                "major_weights": {"Linguistics": 1.0, "Philosophy": 0.7},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                "seen": False
            }
            ]
        }, 
        "International Relations":{
            "major_metadata": {
            "description": "Focuses on global politics, diplomacy, and how nations interact with each other.",
            "filters": ["international relations", "politics", "diplomacy", "culture", "communication"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy learning about diplomacy and how countries interact?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "History": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to work with international organizations and policies?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "Political Science": 0.7},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you like studying how countries cooperate and compete with each other?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "Economics": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                },
                {
                    "question_text": "Would you enjoy analyzing global issues such as conflict, diplomacy, or trade?",
                    "cluster_weights": {"Humanities": 1.0},
                    "major_weights": {"International Relations": 1.0, "History": 0.7},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.2},
                    "seen": False
                }
            ]
        }

    }
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
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
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
            'seen':False
        },
        {
        "question_text": "Do you enjoy solving real-world problems by designing technical systems?",
        "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.4, "Business": 0.3, "Humanities": 0.1},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
        'seen':False
        },
        {
        "question_text": "Would you like to work on improving machines, structures, or processes?",
        "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.3, "Business": 0.3, "Humanities": 0.1},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
        'seen':False
        }, 
        {
        "question_text": "Do you see yourself applying physics and math concepts to engineering challenges?",
        "cluster_weights": {"STEM_engineering": 1.0, "STEM_data": 0.5, "Business": 0.2, "Humanities": 0.1},
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
        "seen": False
        },
        {
    "question_text": "Do you enjoy working with electronics, circuits, or signal systems?",
    "cluster_weights": {
        "STEM_engineering": 1.0,
        "STEM_data": 0.4,
        "Business": 0.2,
        "Humanities": 0.1
    },
    "major_weights": {
        "Electrical Engineering": 1.0,
        "Mechanical Engineering": 0.6,
        "Biomedical Engineering": 0.5,
        "Civil Engineering": 0.3
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},

{
    "question_text": "Would you like to design and improve infrastructure like bridges, roads, or buildings?",
    "cluster_weights": {
        "STEM_engineering": 1.0,
        "STEM_data": 0.3,
        "Business": 0.2,
        "Humanities": 0.1
    },
    "major_weights": {
        "Civil Engineering": 1.0,
        "Mechanical Engineering": 0.7,
        "Electrical Engineering": 0.5,
        "Biomedical Engineering": 0.4
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
},
{
    "question_text": "Do you enjoy working on biomedical devices, prosthetics, or healthcare technology?",
    "cluster_weights": {
        "STEM_engineering": 1.0,
        "STEM_data": 0.3,
        "Business": 0.2,
        "Humanities": 0.1
    },
    "major_weights": {
        "Biomedical Engineering": 1.0,
        "Mechanical Engineering": 0.6,
        "Electrical Engineering": 0.5,
        "Civil Engineering": 0.4
    },
    "answer_weights": {
        "Yes": 0.9,
        "Mostly": 0.6,
        "Sometimes": 0.2,
        "Not really": -0.1,
        "No": -0.2
    },
    "seen": False
}

    ],
    "majors":{
        'Mechanical Engineering':{
            "major_metadata": {
                "description": "Focuses on designing and optimizing machines, vehicles, and mechanical systems.",
                "filters": ["mechanical", "design", "physics", "energy", "manufacturing"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working with engines, machines, or robotics?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Electrical Engineering": 0.6},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.4,"Not really":-0.2,"No":-.3}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to design and test new mechanical devices?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Biomedical Engineering": 0.5},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-.3}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you enjoy solving problems related to motion, energy, and force?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Civil Engineering": 0.5},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-.3},
                    "seen": False
                },
                {
                    "question_text": "Would you like to work on designing vehicles, engines, or industrial equipment?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Mechanical Engineering": 1.0, "Electrical Engineering": 0.6},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-0.3},
                    "seen": False
                }
            ]
        },
        "Electrical Engineering":{
            "major_metadata": {
            "description": "Focuses on circuits, electronics, power systems, and communication technologies.",
            "filters": ["electrical", "circuits", "electronics", "signal processing", "energy"]
            },

            "major_questions": [
                {
                    "question_text": "Do you enjoy working with electronics, circuits, or power systems?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Mechanical Engineering": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-.3}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to work on renewable energy or communication technologies?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Civil Engineering": 0.4},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-.3}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you enjoy working with circuits, electronics, or power systems?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Mechanical Engineering": 0.5},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-0.3},
                    "seen": False
                },
                {
                    "question_text": "Would you like to design systems involving renewable energy or communications?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Electrical Engineering": 1.0, "Biomedical Engineering": 0.6},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-0.3},
                    "seen": False
                }
            ]
        }, 
        "Civil Engineering":{
            "major_metadata": {
            "description": "Focuses on designing and constructing infrastructure such as bridges, roads, and buildings.",
            "filters": ["civil", "infrastructure", "design", "construction", "environment"]
            },
            "major_questions": [
                {
                    "question_text": "Do you enjoy working on construction projects or infrastructure design?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0, "Mechanical Engineering": 0.5},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-0.3}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to improve urban planning or environmental sustainability through engineering?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.2,"No":-.3}, 
                    'seen':False
                }, 
                {
                    "question_text": "Do you enjoy planning and designing buildings, roads, or bridges?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0, "Mechanical Engineering": 0.6},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3},
                    "seen": False
                },
                {
                    "question_text": "Would you like to work on solving environmental or infrastructure challenges?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Civil Engineering": 1.0, "Biomedical Engineering": 0.4},
                    "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3},
                    "seen": False
                }
            ]
        }, 
        "Biomedical Engineering":{
                        "major_metadata": {
                "description": "Focuses on applying engineering to healthcare, including medical devices and biotechnology.",
                "filters": ["biomedical", "healthcare", "devices", "bioengineering", "innovation"]
            },
                        "major_questions": [
                {
                    "question_text": "Do you enjoy combining biology and engineering to solve medical problems?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Biomedical Engineering": 1.0, "Data Science": 0.5},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3}, 
                    'seen':False
                },
                {
                    "question_text": "Would you like to design medical devices or prosthetics?",
                    "cluster_weights": {"STEM_engineering": 1.0},
                    "major_weights": {"Biomedical Engineering": 1.0, "Mechanical Engineering": 0.6},
                    "answer_weights": {"Yes":.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3}, 
                    'seen':False
                }, 
                {
                "question_text": "Do you like combining engineering with medicine to improve healthcare?",
                "cluster_weights": {"STEM_engineering": 1.0},
                "major_weights": {"Biomedical Engineering": 1.0, "Electrical Engineering": 0.6},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3},
                "seen": False
            },
            {
                "question_text": "Would you enjoy designing medical devices such as prosthetics or imaging equipment?",
                "cluster_weights": {"STEM_engineering": 1.0},
                "major_weights": {"Biomedical Engineering": 1.0, "Mechanical Engineering": 0.6},
                "answer_weights": {"Yes":0.8,"Mostly":0.5,"Sometimes":0.3,"Not really":-0.1,"No":-.3},
                "seen": False
            }
            ]
        }
    }
}
