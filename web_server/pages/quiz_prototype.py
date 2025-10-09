#TRUE
# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
import requests
# from web_server.auth  import save_quiz_result
import json
# ---------------------- PAGE CONFIG ----------------------
try:
    im = Image.open(rf"Find_yourself\web_server\logo-round.png")
except Exception:
    im = None

st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)
API_URL ="https://b19e33956c16.ngrok-free.app"
# ---------------------- STYLES ----------------------

st.markdown(
    """
    <style>
    div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
    background-color: #805CD2 !important;
    border-color: #805CD2 !important;
    }
    div[role="radiogroup"] label div:hover {
        transform: scale(1.03);
        border-color: #9448C6 !important;
    }
    div[role="radiogroup"] label div {
        transition: all 0.2s ease-in-out;
    }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #696CDD, #805CD2, #9448C6, #69338C);
        min-height: 100vh;
        -webkit-font-smoothing:antialiased;
        -moz-osx-font-smoothing:grayscale;
        padding-top: 40px;
        padding-bottom: 40px;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #696CDD, #805CD2, #9448C6, #69338C);
    }
    .block-container {
        background: #ffffff;
        border-radius: 16px;
        padding: 12px 20px;
        max-width: 900px;
        margin: 0 auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }
    div.stButton > button, div.stFormSubmitButton > button {
        background: linear-gradient(135deg, #805CD2, #9448C6) !important;
        color: white;
        font-weight: 600;
        border-radius: 12px;
        border: none;
        min-width: 120px;
        cursor: pointer;
        transition: all 0.18s ease-in-out;
    }
    div[data-testid="stMarkdownContainer"] > p strong {
        font-size: 25px;   
        display: inline-block;
    }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        transform: scale(1.05);
    }
    #MainMenu {visibility: hidden;}
    header {
        background-color: transparent !important;
        box-shadow: none !important;
    }
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
# ---------------------- QUIZ DATA ----------------------
quiz = [
    {"question": " What is more related to you?", "options": ["work with nature","work with people","work with technics","work with art","work with symbols"]},
    {"question": " Do you feel comfortable working in team?", "options": ["Yes, I love communication","Mostly, but sometimes alone","Sometimes, It depends","Not Really, but would like to get some help","No, I’d rather do it alone"]},
    {"question": " Do you enjoy solving mathematical and computer problems?", "options": ["Yes, I do","Mostly, but not good with computers","Sometimes, It depends","Not Really, but like technologies","No, it’s not for me"]},
    {"question": " Are you comfortable adapting quickly when things don't go as planned?", "options": ["Yes, I adapt fast and calm","Mostly, but stress affects me","Sometimes, It depends","Not Really, but I good manage stress","No, I prefer stable and predictable situation"]},
    {"question": " Are you interested in learning how the human body and nature works?", "options": ["Yes, It's really interesting","Mostly, but prefer help people","Sometimes, It depends","Not Really, but I'm a bit afraid of medical tools","No, It's not mine"]},
    {"question": " Do you usually understand what others feel and how to respond emotionally?", "options": ["Yes, I'm very sensitive","Mostly, but hard to understand other","Sometimes, It depends","Not Really, but I understand people well","No, I'm kinda robot"]},
    {"question": " Do you enjoy managing finances and running projects?", "options": ["Yes, It's really interests me","Mostly, but I'm not good in math","Sometimes, It depends","Not Really, but I'm a good mathematician","No, It's all hard for me"]},
    {"question": " Do you often come up with new ideas and enjoy experimenting with them?", "options": ["Yes, I'm very creative","Mostly, but not with new things","Sometimes, It depends","Not Really, but new stuff is mine passion","No, I'm not that open-minded"]},
    {"question": " Do you enjoy learning languages, exploring culture and history?", "options": ["Yes, It's very interesting","Mostly, but I prefer learning languages only","Sometimes, It depends","Not Really, but I like exploring culture","No, I don't enjoy writing or the past"]},
    {"question": " Do you enjoy leading people and organizing processes?", "options": ["Yes, I love lead and being responsible","Mostly, but I'm bad at managing tasks","Sometimes, It depends","Not Really, but I can manage tasks well","No, I’d rather be a part of the machine"]},
    {"question": " Do you like working with visuals, sounds and building artistic things?", "options": ["Yes, I’m pretty creative in these areas","Mostly, but hard in realization","Sometimes, It depends","Not Really, but I can bring others' ideas to life","No, that’s absolutely not me"]},
]
# ---------------------- SESSION STATE ----------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = {q["question"]: None for q in quiz}

def transform_response(response):
    return f""""{str(response)}"""

q_index = st.session_state.current_question
last_index = len(quiz) - 1
placeholder = st.empty()
# ---------------------- MAIN ----------------------
def go_next():
    st.session_state.answers[question["question"]] = st.session_state[radio_key]
    if st.session_state.current_question < last_index:
        st.session_state.current_question += 1

def go_prev():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

def clean_text(text: str) -> str:
    # Remove Markdown symbols: ###, **, and quotes
    text = re.sub(r'###', '', text)       # remove all ###
    text = re.sub(r'\*\*', '', text)      # remove all **
    text = text.replace('"', '')           # remove quotes

    # Strip leading/trailing spaces per line and remove empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Rejoin lines with single newlines
    return "\n".join(lines)



import re

def split_sections(text: str) -> dict:
    # Use headings to split sections
    headings = ["Your Hard Skills", "Your Soft Skills", "Your Overall Profile", "Possible Career-Study Directions"]
    pattern = '|'.join([re.escape(h) for h in headings])
    
    # Split while keeping headings
    parts = re.split(f'({pattern})', text)
    
    sections = {}
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        content = parts[i+1].strip()
        sections[title] = content
    return sections

def do_submit():
    st.session_state.answers[question["question"]] = st.session_state[radio_key]
    submitted_answers = st.session_state.answers.copy()    # copies the answers to work with (dict. format)
    # save_quiz_result(st.session_state["user"]["localId"], st.session_state.answers)
    pailor = {"prompt":f"{submitted_answers}"}
    response = requests.post(
        f"{API_URL}/check_data",
        json=pailor
    )
    if response.status_code == 200:
        q_a=response.json()['response']  
    else:
        print('Error')
    q_a=transform_response(q_a)

    payload={"prompt":f'{q_a}'}
    profile=requests.post(f"{API_URL}/generate", json=payload)

    if profile.status_code == 200:
        result = profile.json()['response']
        result=clean_text(result)
        st.session_state["profile_result"] = split_sections(result)
        st.session_state["go_to_profile"] = True
        print(type(result))
        print(result)
        print(st.session_state["profile_result"])
    else:
        placeholder.error("Error")
# ---------------------- PAGE CONTENT ----------------------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Roboto&display=swap" rel="stylesheet">
    <h1 style="
        margin-bottom: -10px;
        font-family: 'Montserrat', 'Roboto', sans-serif;
        letter-spacing: -0.5px;
        font-weight: 800;
        font-size: 48px;
        color: #111;
        text-align: center;
    ">
        Find Yourself Quiz
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h2 style='font-size:24px; color: grey; margin-top:0px; margin-bottom:0px; text-align:left;'>Progress</h2>",
    unsafe_allow_html=True,
)

answered = sum(1 for a in st.session_state.answers.values() if a is not None)
progress = answered / len(quiz)
st.progress(progress)

question = quiz[q_index]
prev_answer = st.session_state.answers[question["question"]]
radio_key = f"q{q_index}"
if radio_key not in st.session_state:
    st.session_state[radio_key] = prev_answer

answer = st.radio(
    f"**{q_index+1}) {question['question']}**",
    question["options"],
    key=radio_key
)

st.markdown(f"<div style='text-align:center; color:grey; margin-bottom:12px;'>Done: {answered}/{len(quiz)}</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    c1, space, c2 = st.columns([1, 0.2, 1])
    with c1:
        st.button("← Previous", use_container_width=True, on_click=go_prev)
    with c2:
        if q_index < last_index:
            st.button("Next →", use_container_width=True, on_click=go_next)
        else:
            st.button("Submit", use_container_width=True, on_click=do_submit)

if st.session_state.get("go_to_profile"):
    st.session_state.pop("go_to_profile")
    st.switch_page("pages/profile_prototype.py")