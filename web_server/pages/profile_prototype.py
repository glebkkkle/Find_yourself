# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
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
# ---------------------- STYLE ----------------------
st.markdown(
    """
    <style>
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
    header {
        background-color: transparent !important;
        box-shadow: none !important;
    }
    footer {visibility: hidden;}
    </style>""", unsafe_allow_html=True)
# ---------------------- PAGE ----------------------
st.markdown("<h1 style='text-align: center; color: black;'>Your Profile</h1>", unsafe_allow_html=True)
st.write("Text")

if "profile_result" in st.session_state:
   st.write(st.session_state["profile_result"])
else:
   st.warning("No profile data available yet. Please complete the quiz.")

if "result" in st.session_state and st.session_state.result:
    st.write(st.session_state.result)
else:
    st.warning("No profile data yet. Please complete the quiz.")

#st.expander("Hard Skills:", expanded=True)
#st.expander("Soft Skills:", expanded=True)
#st.expander("Overall Profile:", expanded=True)