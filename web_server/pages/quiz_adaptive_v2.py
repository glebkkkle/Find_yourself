#TRUE
# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
import requests
from web_server.pages.auth1  import save_quiz_result1, login_user
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
API_URL = "https://4a862f13764b.ngrok-free.app/start_cluster_quiz"
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

# ---------------------- SESSION STATE ----------------------
if "answers1" not in st.session_state:
    st.session_state.answers1 = None
if "current_question1" not in st.session_state:
    st.session_state.current_question1 = None
if "done" not in st.session_state:
    st.session_state.done = False
if "result" not in st.session_state:
    st.session_state.result = None
if "options" not in st.session_state:
    st.session_state.options = {}

login_result = login_user()
if "error" not in login_result:
    st.session_state["uid"] = login_result["localId"]

uid = st.session_state.get("uid")
def transform_response(response):
    return f""""{str(response)}"""
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
# ------------------ FUNCTIONS ------------------
def fetch_next_question():
    payload = {"answer": st.session_state.answers1, "user_id": 'uid'}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()

        if data.get("stage") == "done":
            st.session_state.done = True
            st.session_state.result = data["profile"]
            save_quiz_result1()
            st.switch_page(r"pages\profile_prototype.py")
        else:
            st.session_state.current_question1 = data['question']
            st.session_state.options=data['options']

    else:
        st.error("Error!")
 
def answer_sub():
    payload = {"answer": st.session_state.answers1, "user_id": 'uid'}

    response = requests.post("https://4a862f13764b.ngrok-free.app/answer",json=payload)

    return response.json()['question'], response.json()['options']

if "initialized" not in st.session_state:
    fetch_next_question()   # fetch first question only once
    st.session_state.initialized = True

if not st.session_state.done:
    q = st.session_state.current_question1
    opts = st.session_state.options
    if q:
        answer = st.radio(q, opts)
        if st.button("Answer"):
            st.session_state.answers1= answer
            new_q, new_o=answer_sub()

            print(new_q, new_o)

            st.session_state.current_question1 = new_q
            st.session_state.options = new_o


            print(st.session_state.current_question1)
            print(st.session_state.options)