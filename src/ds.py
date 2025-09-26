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
<<<<<<< HEAD
                "description": "Focuses on extracting insights from large datasets, predictive modeling, and statistical analysis.",
=======
                "description": "Data Science is a dynamic field designed for individuals who possess a strong analytical mindset, a keen curiosity for uncovering insights from data, and a collaborative spirit. Ideal candidates for this major are those who take pleasure in tackling complex problems, have a propensity for critical thinking, and are comfortable navigating both quantitative and qualitative data. Students who thrive in this discipline often exhibit a blend of technical proficiency and creativity, allowing them to not only analyze data but also to visualize and communicate their findings effectively.\n\nThroughout the Data Science program, students develop a comprehensive set of technical skills and domain knowledge essential for data-driven decision-making. The curriculum includes courses in statistical analysis, machine learning, data mining, and programming languages such as Python and R. Students learn to work with various data tools and platforms, including SQL databases, cloud computing resources, and data visualization software like Tableau or Power BI. They also engage in hands-on projects that deepen their understanding of data wrangling, model building, and algorithmic thinking, equipping them with the expertise to extract actionable insights from large datasets.\n\nIn addition to technical competencies, the program emphasizes the cultivation of vital soft skills that are critical for success in the field. Effective communication, teamwork, and the ability to convey complex data narratives to diverse audiences are integral components of the curriculum. Students develop empathy, enabling them to understand user needs and contextualize their findings within real-world scenarios. Those who are detail-oriented, adaptable, and possess a natural inclination toward continuous learning will find themselves particularly well-suited to thrive in this rapidly evolving landscape.\n\nData Science education is not just about theory; it is firmly rooted in practical application. Students engage in collaborative projects, internships, and case studies that simulate real-world data challenges faced by organizations across various sectors. This hands-on approach prepares graduates to apply their knowledge in meaningful ways, allowing them to bridge the gap between technical solutions and business needs. \n\nAs they complete their studies, graduates of the Data Science program are poised to embark on diverse career paths that involve harnessing data to drive innovation, improve processes, and inform strategic decisions. Whether through developing predictive models, optimizing operations, or providing actionable insights, they are equipped to make impactful contributions in an array of industries, effectively shaping the future of data utilization in society.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
            }
            ]
        },
        "Artificial Intelligence": {
            "major_metadata": {
<<<<<<< HEAD
                "description": "Focuses on algorithms that enable computers to learn, reason, and make decisions.",
=======
                "description": "**Artificial Intelligence  Description**\n\nArtificial Intelligence (AI) is designed for individuals who possess a keen analytical mindset coupled with a creative flair for problem-solving. Those who thrive in this major are naturally curious, technologically inclined, and have a passion for understanding complex systems. This program is ideal for students who are detail-oriented, adaptable to rapid changes, and possess a strong desire to innovate within the realms of technology and human experience.\n\nThroughout the program, students build a robust foundation in core technical skills such as programming (Python, Java, and C++), machine learning algorithms, data structures, and computational theory. They delve into specialized areas including natural language processing, computer vision, and robotics, gaining proficiency in essential tools and methodologies. Through hands-on projects and collaborative research, students apply their technical knowledge to real-world problems, developing domain expertise in AI applications across various industries, from healthcare to finance.\n\nIn addition to technical acumen, the program places a strong emphasis on cultivating soft skills that are critical for success in the field. Students enhance their communication abilities, learn to work effectively in teams, and refine their ethical reasoning in relation to AI's impact on society. Interpersonal skills such as empathy and cultural awareness are fostered, preparing graduates to engage with diverse stakeholders and make decisions that consider both human and technological implications.\n\nIdeal candidates for this major are analytical thinkers who can synthesize information and generate innovative ideas. They are also empathetic communicators who can translate complex technical concepts into understandable formats for varied audiences. Those who embrace challenges, demonstrate resilience, and have a collaborative spirit are particularly suited for the dynamic environment of AI.\n\nThe program prepares students to translate their knowledge into practical applications that address real-world challenges. With opportunities to engage in internships, research projects, and industry partnerships, students develop a portfolio of work that demonstrates their ability to implement AI solutions effectively. Graduates emerge ready to contribute to advancements in technology that enhance human capabilities, create intelligent systems, and improve decision-making processes. The future paths for AI majors are diverse, encompassing roles that bridge technical expertise with social impact, drive innovation, and influence the intersection of technology and society.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
                }
            ]
        },
        "Accounting": {
            "major_metadata": {
<<<<<<< HEAD
                "description": "Focuses on financial reporting, business analytics, and managing monetary data.",
=======
                "description": "Accounting is a dynamic field designed for individuals with a keen eye for detail, strong analytical skills, and an aptitude for understanding financial systems and business operations. Those who excel in this major are methodical thinkers, ethical decision-makers, and problem-solvers who enjoy organizing, interpreting, and presenting financial information accurately. Throughout the program, students gain a comprehensive foundation in financial accounting, managerial accounting, auditing, taxation, and financial reporting, as well as proficiency in accounting software and data analysis tools. In addition to technical expertise, the major emphasizes critical thinking, effective communication, and professional ethics, preparing students to navigate complex financial scenarios and make informed decisions. Practical experiences through internships, case studies, and collaborative projects enable students to apply theoretical knowledge in real-world contexts, enhancing their understanding of business operations and regulatory compliance. Graduates of the Accounting major are well-equipped to pursue careers in public accounting, corporate finance, auditing, consulting, or financial management, contributing to organizations by ensuring transparency, accuracy, and strategic insight in financial practices.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
                }   
            ]
        },
        "Data Analytics": {
            "major_metadata": {
<<<<<<< HEAD
                "description": "Focuses on analyzing business and operational data to provide actionable insights.",
=======
                "description": "Data Analytics is an interdisciplinary field designed for individuals with a strong curiosity for extracting insights from complex data and a passion for solving real-world problems through quantitative reasoning. Those who thrive in this major possess analytical thinking, attention to detail, and proficiency in statistics, programming, and data visualization tools. Throughout the program, students develop expertise in data collection, cleaning, modeling, and interpretation, as well as proficiency with software such as Python, R, SQL, and business intelligence platforms. In addition to technical skills, the major emphasizes critical thinking, effective communication, and the ability to translate data into actionable insights that inform strategic decision-making. Practical experiences through projects, internships, and collaborative case studies allow students to apply methodologies in various industries, from finance and healthcare to marketing and technology. Graduates are well-prepared for careers as data analysts, business analysts, data scientists, or consultants, contributing to organizations by turning raw data into meaningful insights, driving efficiency, and supporting data-informed strategies across diverse domains.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on managing organizations, leadership, operations, and decision-making in business contexts.",
=======
                "description": "Business Administration is a versatile field designed for individuals with strong leadership potential, strategic thinking, and a passion for understanding organizational dynamics and decision-making processes. Those who excel in this major are analytical, adaptable, and effective communicators, capable of managing teams, projects, and resources efficiently. Throughout the program, students gain expertise in management principles, finance, marketing, operations, human resources, and entrepreneurship, while also developing proficiency in business analytics, strategic planning, and organizational behavior. The major emphasizes critical thinking, ethical decision-making, and collaborative problem-solving, preparing students to navigate complex business challenges. Practical experiences through internships, case studies, and group projects allow students to apply theoretical knowledge in real-world contexts, fostering leadership and management skills. Graduates of the Business Administration major are well-equipped for careers in corporate management, consulting, entrepreneurship, or public administration, contributing to organizations by driving growth, innovation, and operational excellence.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on market behavior, economic theory, and data-driven decision-making in societies and businesses.",
=======
                "description": "Economics is designed for individuals who possess a keen analytical mindset and a fascination with understanding how societies allocate resources and make decisions. Ideal candidates are those who enjoy problem-solving, critical thinking, and are curious about the intricacies of market behaviors, consumer choices, and the impact of public policies on economic welfare. Students in this major are drawn to quantitative analysis and excel at interpreting complex data, making it a perfect fit for detail-oriented and logically minded individuals who are also adept at communicating their insights effectively.\n\nThroughout the program, students develop a comprehensive skill set that includes proficiency in statistical analysis, econometrics, and modeling economic theories. They learn to utilize various tools and software, such as STATA, R, and Excel, to analyze data and forecast economic trends. The curriculum covers a wide range of topics, including microeconomics, macroeconomics, international economics, and behavioral economics, providing a robust understanding of both theoretical frameworks and practical applications within the economic landscape. This technical foundation equips students with the skills necessary to dissect economic indicators, evaluate market dynamics, and assess the effects of government policies.\n\nIn addition to technical expertise, the program places a strong emphasis on cultivating essential soft skills. Effective communication, teamwork, and ethical reasoning are fundamental for success in economics, where collaboration across various disciplines is often necessary. Students develop the ability to articulate complex economic concepts to diverse audiences, fostering a skill set that is vital for influencing policy, conducting impactful research, and engaging with the public on economic issues. Those who thrive in this program are typically analytical thinkers who can empathize with varied perspectives, use creativity to explore alternative solutions, and approach challenges with resilience and adaptability.\n\nThe Economics program engages students in real-world applications through case studies, internships, and collaborative projects that bridge theoretical knowledge with practical experience. By analyzing real economic problems and proposing data-driven solutions, graduates are well-prepared to navigate the complexities of economic systems and contribute meaningfully to their fields. \n\nUpon completion, students find themselves equipped to pursue a myriad of paths that contribute to economic innovation and societal advancement. Whether through influencing public policy, conducting research that informs economic strategy, or applying analytical and critical thinking skills to address pressing global challenges, graduates of Economics are positioned to make significant impacts that foster sustainable development and enrich community well-being.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on investment, corporate finance, and financial markets to optimize resource allocation.",
=======
                "description": "Finance is a rigorous field designed for individuals with strong analytical skills, numerical proficiency, and a keen interest in understanding financial markets, investments, and corporate financial management. Those who excel in this major are critical thinkers, problem-solvers, and detail-oriented professionals capable of evaluating complex financial data and making informed decisions. Throughout the program, students gain expertise in investment analysis, corporate finance, risk management, financial modeling, and portfolio management, while also developing proficiency in financial software, quantitative methods, and regulatory compliance. The major emphasizes strategic thinking, ethical decision-making, and effective communication, preparing students to navigate dynamic financial environments. Practical experiences through internships, case studies, and collaborative projects allow students to apply theoretical knowledge in real-world settings, fostering strong analytical and decision-making skills. Graduates of the Finance major are well-equipped for careers in investment banking, corporate finance, financial planning, asset management, or consulting, contributing to organizations by optimizing financial performance and supporting strategic growth.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on leadership, organizational behavior, and decision-making in teams and companies.",
=======
                "description": "Management is a dynamic field designed for individuals with strong leadership abilities, strategic thinking, and a passion for guiding teams and organizations toward achieving goals. Those who excel in this major are effective communicators, problem-solvers, and decision-makers capable of analyzing organizational processes and implementing efficient solutions. Throughout the program, students gain expertise in project management, organizational behavior, operations, human resources, strategic planning, and entrepreneurship, while developing proficiency in business analytics and performance measurement tools. The major emphasizes leadership, ethical decision-making, teamwork, and adaptability, preparing students to navigate complex organizational challenges. Practical experiences through internships, case studies, and collaborative projects allow students to apply theoretical knowledge in real-world contexts, fostering managerial skills and strategic insight. Graduates of the Management major are well-equipped for careers in corporate management, consulting, operations, human resources, or entrepreneurship, contributing to organizations by optimizing performance, driving innovation, and leading teams effectively.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
        "description": "Focuses on understanding past events, civilizations, and their impact on society.",
=======
        "description": "**History  Description**\n\nThe History major is designed for individuals who possess a deep curiosity about the past and an innate desire to understand the complexities of human experience. Ideal candidates are critical thinkers with strong analytical skills and an affinity for research, storytelling, and contextual analysis. Students in this program are encouraged to engage with diverse historical narratives and develop a nuanced appreciation for the socio-political, cultural, and economic forces that shape societies across time.\n\nThroughout the program, students acquire a robust set of technical skills, including advanced research methodologies, archival skills, and proficiency in historical analysis. Coursework encompasses a range of topics, from ancient civilizations to modern global issues, and often includes training in historiography, digital history tools, and quantitative analysis of historical data. This interdisciplinary approach equips students with the ability to examine primary and secondary sources critically and to construct well-founded historical arguments.\n\nIn addition to technical expertise, the History major fosters essential soft skills that are crucial for success in this field, such as effective communication, persuasive writing, and the ability to engage in thoughtful debate. Students learn to articulate complex ideas clearly and to empathize with diverse perspectives, skills that are vital when collaborating with others or presenting findings. Those who are meticulous, open-minded, and enjoy uncovering hidden narratives within historical contexts tend to thrive in this program.\n\nThrough immersive learning experiences such as research projects, internships, and community-engaged history projects, graduates have the opportunity to apply their knowledge in practical, real-world settings. They explore ways to interpret and present history, fostering a deeper understanding of societal issues and cultural heritage. Individuals who are passionate about connecting past events to contemporary issues, advocating for social justice, and inspiring others through historical inquiry will find this major particularly fulfilling.\n\nPotential future paths may involve contributing to cultural preservation, enhancing public understanding of history through education or media, or engaging in policy-making that draws on historical insights. The History major prepares students to blend their analytical capabilities with their passion for human stories, empowering them to make meaningful contributions to society by interpreting and contextualizing the ever-evolving tapestry of human history.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
            "description": "Focuses on critical thinking, ethics, reasoning, and the study of knowledge and existence.",
=======
            "description":  "Philosophy is designed for individuals who possess a deep curiosity about fundamental questions concerning existence, knowledge, values, and human nature. Ideal candidates are critical thinkers who enjoy engaging in abstract reasoning and have a propensity for questioning assumptions. They are often empathetic communicators, capable of understanding diverse perspectives and articulating complex ideas clearly. Those who thrive in this major tend to be reflective, detail-oriented, and willing to explore challenging concepts, making them well-suited for the rigorous analytical demands of philosophical inquiry.\n\nThroughout the program, students develop a robust foundation in various areas of philosophical thought, including ethics, metaphysics, epistemology, and logic. They engage with classical and contemporary texts, honing their abilities in critical analysis and argumentation. Courses often involve examining the works of influential philosophers, participating in debates, and utilizing tools like formal logic and philosophical writing techniques. This intellectual rigor equips students with the skills to dissect intricate arguments and forge their own philosophical perspectives.\n\nIn addition to technical knowledge, the study of philosophy fosters essential soft skills such as effective communication, active listening, and ethical reasoning. Students learn to navigate complex moral dilemmas, advocate for their viewpoints while respecting opposing views, and collaboratively engage with peers in discussions. These interpersonal skills are crucial for success in any field, particularly in roles that require negotiation, leadership, or community engagement.\n\nPhilosophy majors typically thrive on exploring the intersections of various disciplines and applying their insights to real-world issues. Through critical discussions, collaborative projects, and reflective writing, they engage with contemporary societal challenges and explore the implications of philosophical thought in practical contexts. Those who enjoy examining life's profound questions, developing compelling arguments, and seeking to understand the human condition will find the program particularly fulfilling.\n\nGraduates of the Philosophy program are well-prepared to pursue diverse paths that allow them to contribute to innovative thought, apply critical analysis to societal issues, and bridge the gap between theoretical frameworks and practical applications. Whether influencing public policy, engaging in ethical advocacy, or pursuing careers in education, law, or social services, philosophy graduates are positioned to make substantial contributions by applying their philosophical insights to foster understanding and positive change in the world.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on the scientific study of language, its structure, and its role in communication.",
=======
                "description": "Linguistics is a dynamic field designed for individuals who possess a deep curiosity about language and its intricate structures, meanings, and social functions. It appeals to those who are analytical thinkers, empathetic communicators, and detail-oriented problem-solvers, eager to explore the nuances of human communication and its impact on society. Students who excel in this program often have a passion for understanding diverse languages and cultures, and they thrive on the intellectual challenge of dissecting language patterns, syntax, phonetics, and semantics.\n\nIn this program, students develop a strong foundation in various linguistic disciplines, including phonology, morphology, syntax, semantics, and sociolinguistics. Engaging with advanced analytical tools, such as computational linguistics and language documentation software, students learn to employ qualitative and quantitative research methods to analyze linguistic data. The curriculum is designed to foster domain expertise in the structure and use of language, enabling students to conduct thorough investigations into language phenomena and their implications across different contexts.\n\nAlongside technical skills, the program emphasizes the cultivation of essential soft skills, including effective communication, critical thinking, and collaborative teamwork. Students learn to articulate complex linguistic concepts clearly and persuasively, which is crucial for engaging with diverse audiences in academic, professional, and community settings. The ability to empathize with speakers of different languages and dialects is also cultivated, enhancing students capacity to work in multilingual and multicultural environments. Those who are adaptable, curious, and committed to ongoing learning will find themselves well-suited to this field.\n\nThe Linguistics program prepares students to apply their knowledge in real-world contexts through hands-on projects, fieldwork, and interdisciplinary collaborations. Students engage in practical applications, such as analyzing language use in social media, developing language teaching materials, or participating in community language revitalization efforts. Graduates emerge with a comprehensive understanding of how language shapes human experience and societal structures, positioning them to bridge gaps between linguistic theory and practical realities.\n\nPotential future paths for graduates include contributing to innovations in language technology, enhancing communication strategies in diverse settings, or promoting linguistic equity and understanding in multicultural environments. Linguistics empowers students to blend their analytical insights with social awareness, ultimately preparing them to make significant contributions to the study and application of language in a rapidly evolving world.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
            "description": "Focuses on global politics, diplomacy, and how nations interact with each other.",
=======
            "description": "International Relations is a dynamic and interdisciplinary major designed for individuals with a passion for understanding global affairs, cultural diversity, and international diplomacy. Ideal candidates possess a blend of analytical thinking, strong communication skills, and an innate curiosity about the complexities of the world. Students who thrive in this program are often detail-oriented, empathetic, and skilled at considering multiple perspectives, making them well-suited for examining the intricacies of international systems and relationships.\n\nThroughout the program, students gain a robust foundation in essential areas such as political theory, global governance, conflict resolution, and international economics. Coursework may include studies in international law, foreign policy analysis, and global security, supplemented by practical skills in research methodology, data analysis, and negotiation strategies. Students also become proficient in using tools such as Geographic Information Systems (GIS) for spatial analysis and various research platforms to access and interpret global data. This technical knowledge is critical for understanding and addressing contemporary global challenges.\n\nIn addition to technical expertise, the program emphasizes the development of soft skills that are vital for success in international settings. Students refine their ability to engage in cross-cultural communication, work collaboratively in diverse teams, and navigate complex ethical dilemmas. Leadership, adaptability, and critical thinking are also fostered, enabling students to approach global issues with a multifaceted mindset. Those who excel in this program often possess a genuine interest in connecting with others, advocating for justice, and finding innovative solutions to global problems.\n\nThrough experiential learning opportunities such as internships, model United Nations simulations, and study-abroad programs, students apply their knowledge in real-world contexts, engaging with global communities and institutions firsthand. This practical experience not only enhances their understanding of international dynamics but also equips them with the tools to influence positive change on a global scale. \n\nGraduates of the International Relations program are well-prepared to embark on diverse paths that contribute to global understanding and cooperation. They may find themselves working to bridge cultural divides, drive policy initiatives, or facilitate dialogue among nations, all while leveraging their analytical skills and human-centered approach to tackle some of the most pressing challenges facing the international community today.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                "description": "Focuses on designing and optimizing machines, vehicles, and mechanical systems.",
=======
                "description": "Mechanical Engineering is designed for individuals who possess a strong analytical mindset coupled with a creative flair for problem-solving. Those who thrive in this program often exhibit traits such as curiosity about how things work, resilience in tackling complex challenges, and a passion for innovation. Ideal candidates are detail-oriented, enjoy hands-on learning, and have a keen interest in applying mathematics, physics, and engineering principles to design and improve mechanical systems.\n\nThroughout the program, students acquire a robust technical foundation encompassing core subjects such as thermodynamics, fluid mechanics, materials science, and dynamics. They gain proficiency in computer-aided design (CAD) software, simulation tools, and manufacturing processes, which are essential for creating and analyzing mechanical components and systems. Students engage in rigorous coursework and practical labs that foster an understanding of engineering principles while also exploring emerging technologies such as robotics and sustainable energy solutions.\n\nIn addition to technical knowledge, the curriculum emphasizes the development of vital soft skills such as teamwork, effective communication, project management, and ethical reasoning. These skills are critical for navigating the collaborative and interdisciplinary nature of engineering projects, where the ability to articulate ideas and work well with diverse teams is paramount. Students who excel in this environment are often those who possess a strong sense of initiative, adaptability, and an appreciation for continuous learning.\n\nThe Mechanical Engineering program prepares students to apply their knowledge in real-world contexts through hands-on projects, internships, and cooperative education opportunities. By working on practical challenges that require innovative thinking and collaboration, students learn to bridge theoretical concepts with tangible outcomes, designing solutions that meet the needs of society while considering economic and environmental impacts.\n\nGraduates of this program can look forward to diverse future paths that involve contributing to advancements in technology, enhancing product design and efficiency, and driving innovation across various industries. By integrating their technical expertise with strong interpersonal abilities, they are well-equipped to address complex challenges, create sustainable solutions, and lead initiatives that improve both mechanical systems and the human experience.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
            "description": "Focuses on circuits, electronics, power systems, and communication technologies.",
=======
            "description": "Electrical Engineering is designed for individuals who possess a strong analytical aptitude, a passion for innovation, and an innate curiosity about how electrical systems and technologies can shape our modern world. Ideal candidates are often detail-oriented, methodical thinkers who enjoy tackling complex problems and have a creative approach to designing solutions. Those who thrive in this major are typically drawn to understanding the principles of electricity, electronics, and electromagnetism, and have a keen interest in applying this knowledge to develop cutting-edge technologies and systems.\n\nThroughout the program, students cultivate a robust set of technical skills, including circuit design, signal processing, and control systems, complemented by proficiency in software tools such as MATLAB, LabVIEW, and various programming languages. The curriculum encompasses a range of topics, from power systems and microelectronics to telecommunications and embedded systems, providing a comprehensive understanding of both the theoretical and practical aspects of electrical engineering. Students engage in hands-on laboratory experiences, enabling them to apply theoretical concepts to real-world scenarios and gain expertise in both simulation and physical prototyping.\n\nIn addition to technical competencies, the program emphasizes the development of vital soft skills, including effective communication, teamwork, and project management. Electrical engineers often collaborate with professionals from diverse fields, making the ability to convey complex ideas clearly and work collaboratively essential for success. Students are encouraged to hone their problem-solving abilities and ethical reasoning, preparing them to navigate the challenges that arise in engineering projects while maintaining a focus on the societal impact of their work.\n\nGraduates of this program are well-equipped to apply their knowledge in practical contexts, often engaging in team-based projects that simulate real industry challenges. They learn to approach problems with a mindset focused on innovation, sustainability, and the user experience, which enhances their ability to deliver practical solutions that meet the demands of a rapidly evolving technological landscape. \n\nPotential future paths for graduates include driving advancements in renewable energy, enhancing communication technologies, or revolutionizing consumer electronics, all while contributing to the development of systems that improve efficiency and quality of life. Electrical Engineering prepares students to merge their technical expertise with a forward-thinking perspective, empowering them to make significant contributions to technology and society.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
            "description": "Focuses on designing and constructing infrastructure such as bridges, roads, and buildings.",
=======
            "description": "Civil Engineering  Description\n\nCivil Engineering is designed for individuals who are inherently curious about the physical world and possess a strong analytical mindset, coupled with a knack for problem-solving and a commitment to improving the infrastructure that shapes our communities. Ideal candidates for this major are detail-oriented, creative thinkers who enjoy math and science, and have a passion for developing sustainable solutions to complex engineering challenges. This program prepares students to understand the principles of design, construction, and maintenance of various infrastructures, such as roads, bridges, buildings, and water supply systems.\n\nStudents in the Civil Engineering program develop a robust technical skill set that includes proficiency in structural analysis, fluid mechanics, geotechnics, and materials science. They gain hands-on experience with advanced tools and software, such as AutoCAD, MATLAB, and civil engineering simulation platforms, which are essential for designing and modeling engineering projects. The curriculum is designed to integrate theoretical knowledge with practical application, ensuring that students are well-versed in industry standards, regulations, and sustainability practices crucial for modern engineering endeavors.\n\nIn addition to technical expertise, the program fosters vital soft skills such as effective communication, teamwork, and project management. Civil engineers often work in multidisciplinary teams, and the ability to convey complex ideas clearly, listen actively, and collaborate with others is paramount to success. Students who are adaptable, possess strong leadership potential, and are committed to ethical practices in engineering will find themselves thriving in this dynamic field.\n\nThrough real-world projects, internships, and community-focused initiatives, graduates of this program learn to apply their knowledge in practical contexts, addressing real-life challenges in urban planning, environmental sustainability, and infrastructure resilience. Those who enjoy taking initiative, working collaboratively, and making a tangible impact on society will find this major particularly fulfilling.\n\nPotential future paths for Civil Engineering graduates encompass a broad range of opportunities, including driving innovation in sustainable infrastructure, improving public safety through efficient design, and enhancing the quality of life in communities through smart engineering solutions. Civil Engineering equips students with the skills and knowledge necessary to effectively bridge technical and human considerations, ensuring their contributions lead to safer, more sustainable, and resilient environments.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
                        "major_metadata": {
                "description": "Focuses on applying engineering to healthcare, including medical devices and biotechnology.",
=======
            "major_metadata": {
                "description":  "Biomedical Engineering  Description\n\nBiomedical Engineering is tailored for individuals who possess a strong foundation in both engineering principles and biological sciences, along with an innate curiosity about enhancing patient care through technological innovation. This program is ideal for those who are analytical thinkers, detail-oriented, and have a passion for problem-solving in complex healthcare challenges. Students are equipped with the technical skills and knowledge necessary to navigate the interdisciplinary landscape of medicine and engineering, learning core concepts in mechanics, materials science, and bioinstrumentation, while also delving into areas such as medical imaging, tissue engineering, and biomaterials.\n\nThroughout the program, students acquire proficiency in various tools and methodologies, including computer-aided design (CAD), finite element analysis, and laboratory techniques relevant to biological systems. The curriculum fosters a deep understanding of human physiology and anatomy, as well as the principles of device design and regulatory considerations in the biomedical field. This technical foundation is complemented by coursework that emphasizes the importance of ethical considerations, safety standards, and the impact of innovations on patient health and wellbeing.\n\nIn addition to technical acumen, Biomedical Engineering nurtures essential soft skills such as effective communication, teamwork, and project management. The ability to work collaboratively with healthcare professionals, engineers, and researchers is crucial in this field, and students cultivate these interpersonal skills through group projects and interdisciplinary initiatives. Individuals who thrive in this program typically exhibit resilience, creativity, and a genuine interest in improving healthcare outcomes through innovation.\n\nThe program emphasizes practical, real-world applications by engaging students in hands-on projects, internships, and partnerships with healthcare institutions and industries. By working on tangible problems, students learn to apply their knowledge to develop solutions that address real healthcare needs, from designing life-saving medical devices to improving diagnostic tools. \n\nGraduates of Biomedical Engineering are well-prepared to forge impactful careers that bridge the gap between technology and healthcare. They are positioned to contribute to advancements in medical technology, enhance patient care processes, and lead initiatives that transform healthcare delivery through innovative engineering solutions. This major empowers students to leverage their expertise in both technical and human-centered approaches, ultimately fostering improved health outcomes in diverse settings.",
>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
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
<<<<<<< HEAD
=======


>>>>>>> 350b64d2b7736334df4866b3334215762e5f2ff7
