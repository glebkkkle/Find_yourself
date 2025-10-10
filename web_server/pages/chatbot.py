import streamlit as st
import requests
from PIL import Image


st.markdown("""
<style>
}
div[data-testid="stButtonGroup"] button {
    background-color: #ffffff !important;  
    color: #000000 !important;             
    border: 0.5px solid #000000 !important;  
    border-radius: 16px !important;         
    padding: 8px 16px !important;
    margin: 4px !important;
    text-align: left !important;           
    font-weight: 500 !important;
}
[data-testid="stChatMessage"] {
    background-color: #cacacaff !important;         
}
div[data-testid="stChatMessageContent"] *{
    color: black !important;
    text-align: left !important;
    font-size: 17px !important;           
}
[data-testid="stChatInput"] > div {
    border: 0.1px solid #000000 !important;  
    border-radius: 30px !important;
    box-shadow: none !important;           
    background-color: #ffffff !important;  
}
div[data-testid="stButtonGroup"] button {
    transition: transform 0.4s ease !important;
}
div[data-testid="stButtonGroup"] button:hover {
    background-color: none !important;
    transform: scale(1.03) !important;
}
[data-testid="stChatInput"] button {
    display: none !important;
}
[data-testid="stChatInput"] {
    background-color: #ffffff !important;
    border-radius: 30px !important;
    border: none !important;
    padding: 6px 10px !important;
    box-shadow: none !important;
}
[data-testid="stChatInput"] > div {
    background-color: #ffffff !important;
    border-radius: 30px !important;
}
[data-testid="stChatInput"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: none !important;
    font-size: 16px !important;
    padding-left: 10px !important;
    box-shadow: inset 0 0 0 1px #ccc !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #888 !important;
}
h1 {
    color: #222 !important;
    font-weight: 700;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #696CDD, #805CD2, #9448C6, #69338C);
    min-height: 100vh;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
    padding-top: 40px;
    padding-bottom: 40px;
}
.block-container {
    background: #ffffff;
    border-radius: 16px;
    padding: 12px 20px;
    max-width: 900px;
    margin: 0 auto;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
}
#MainMenu {visibility: hidden;}
header {background-color: transparent !important; box-shadow: none !important;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

SUGGESTIONS = {
    ":yellow[:material/star:] What are my top strengths?": (
        "Help me understand my main strengths based on my quiz answers and how I can use them in life and work."
    ),
    ":grey[:material/work:] How do I work best?": (
        "Explain whether I perform better in teams, independently, or in creative vs analytical tasks."
    ),
    ":green[:material/trending_up:] How can I grow personally?": (
        "Give me ideas on personal development, skills to improve, and ways to become more adaptable."
    ),
    ":yellow[:material/flash_on:] What motivates me most?": (
        "Help me identify what activities, environments, or goals energize me and make me feel fulfilled."
    ),
    ":blue[:material/people:] How can I use my strengths to help others?": (
        "Suggest ways I can apply my skills and personality to make a positive impact in my community or work."
    ),
}
if "answers" in st.session_state:
    sub_ans = st.session_state.answers
else:sub_ans=None
if "profile_result" in st.session_state:
    prof = st.session_state.profile_result
else:prof=None
if "result" in st.session_state and st.session_state.result:
    adap_res = st.session_state.result 
else: adap_res=None
user_avatar = Image.open(r"user_avatar.jpg")
bot_avatar = Image.open(r"bot_avatar.jpg")

def avatarer():
    if message['role'] == 'assistant':
        return bot_avatar
    if message['role'] == 'user':
        return user_avatar
    
API_URL_CHAT = "https://e3f3759e9a98.ngrok-free.app/chat"
title_row = st.container(
    horizontal=True,
    vertical_alignment="bottom",
)

with title_row:
    st.title(
        "Find Yourself AI assistant", anchor=False, width="stretch"
    )

@st.dialog("Legal disclaimer")
def show_disclaimer():
      st.caption("This AI ChatBot may be innaccurate in some specific topics, so please, ask questions only about your profile and quiz.")

user_init_question = (
    "initial_question" in st.session_state and st.session_state.initial_question
)
user_init_suggestion = (
    "selected_suggestion" in st.session_state and st.session_state.selected_suggestion
)
user_first_interaction = (
    user_init_question or user_init_suggestion
)
has_message_history = (
    "messages" in st.session_state and len(st.session_state.messages) > 0
)

def clear_conversation():
    st.session_state.messages = []

if not user_first_interaction and not has_message_history:
    st.session_state.messages = []
    with st.container():

        user_input = st.chat_input("Ask a question...", key="initial_question")

        selected_suggestion = st.pills(
            label="Examples",
            label_visibility="collapsed",
            options=SUGGESTIONS.keys(),
            key="selected_suggestion",
        )

        st.button(
            "&nbsp;:small[:gray[:material/balance: Legal disclaimer]]",
            type="tertiary",
            on_click=show_disclaimer,
        )
        st.stop()

with st.container():
    res_but = st.container()
    chat_cont = st.container()
    user_message = st.chat_input("Ask a follow-up...")

    with chat_cont:
        for message in st.session_state.messages:
            avatar = avatarer()
            with st.chat_message(message["role"], avatar=avatar):
                if message["role"] == "assistant":
                    st.container()
                st.markdown(message['content'])

        if not user_message:

            if user_init_question:
                user_message = st.session_state.initial_question
            if user_init_suggestion:
                user_message = SUGGESTIONS[st.session_state.selected_suggestion]

        with res_but:
            st.button("Restart", icon=":material/refresh:", on_click=clear_conversation)

        if user_message:
            st.session_state.messages.append({"role": "user", "content": user_message})
            print(st.session_state.messages)
            with st.chat_message('user', avatar=user_avatar):
                st.text(user_message)

            with st.chat_message('assistant', avatar=bot_avatar):
                with st.spinner("Thinking..."):
                    if adap_res is not None or prof is not None or sub_ans is not None:
                        response = requests.post(API_URL_CHAT, json={'session_id':'1', 'query':user_message, "quiz_adap_res": adap_res , "profile": prof, "quiz": sub_ans })
                    else:
                        response = requests.post(API_URL_CHAT, json={'session_id':'1', 'query':user_message})
                    if response.status_code == 200:
                        ai = response.json()['ai_m']
                with st.container():
                    ai_message = st.write(ai)
                    st.session_state.messages.append({"role": "assistant", "content": ai})
            st.rerun()