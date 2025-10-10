#TRUE
# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
import requests
from web_server.pages.auth1 import save_quiz_result1, login_user
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
API_URL = "https://e3f3759e9a98.ngrok-free.app"

from src.quiz_majors import RunPremiumQuizMain, MainLLM

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
if "llm_instance" not in st.session_state:
    st.session_state.llm_instance = MainLLM()

login_result = login_user()
if "error" not in login_result:
    st.session_state["uid"] = login_result["localId"]

uid = st.session_state.get("uid")
if not uid:
    st.error("Pizda")
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
adap_prof = st.container()
def fetch_next_question():
    payload = {"answer": st.session_state.answers1, "user_id": 'uid'}
    response = requests.post(f"{API_URL}/start_cluster_quiz", json=payload)
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

def answer_sub(answer, quiz_instance):

    st.session_state.answer1 = answer

    result = quiz_instance.answer(answer)
    if result is None:
        st.session_state.done = quiz_instance.done
        return None, None, None

    stage, new_q, new_o = result
    st.session_state.done = quiz_instance.done

    return stage, new_q, new_o

if "initialized" not in st.session_state:
    st.session_state.quiz_instance_new1 = RunPremiumQuizMain('new1')

    quiz=st.session_state.quiz_instance_new1

    cl,q,op=quiz.init_quiz('new1')

    st.session_state.current_question1 =q
    st.session_state.options=op

    st.session_state.initialized = True


with adap_prof:
    quiz1 = st.session_state.quiz_instance_new1

    if not st.session_state.done:
        q = st.session_state.current_question1
        opts = st.session_state.options

        if q:
            selected = st.radio(f"**{q}**", opts)
            if st.button("Answer"):
                stage, new_q, new_o = answer_sub(selected, quiz1)

                if stage == 'done':
                    st.session_state.done = True
                    st.session_state.final_major = new_q  
                    st.rerun()
                else:

                    st.session_state.current_question1 = new_q
                    st.session_state.options = new_o
                    st.rerun()
    else:
        final_major = st.session_state.get('final_major', None)
        res=st.session_state.llm_instance.generate_major_suggestion(st.session_state.profile_result, final_major)
        st.session_state.result = res
        st.switch_page(r"pages/profile_prototype.py")


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
    div[data-testid="stWidgetLabel"] label {
        font-size: 25px !important;
        font-weight: 800 !important;
        font-family: 'Montserrat', 'Roboto', sans-serif !important;
        display: inline-block;
        color: #111 !important;
    }
    div[data-testid="stMarkdownContainer"] > p strong {
        font-size: 25px !important;   
        display: inline-block !important;
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


