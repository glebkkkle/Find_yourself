import streamlit as st
from PIL import Image
from auth import register_user, login_user
# ---------------- STYLES ----------------
st.markdown(
    """
    <style>
    div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
    background-color: #805CD2 !important;
    border-color: #805CD2 !important;
    }
    input[type="text"], input[type="password"] {
        background-color: #d1d1d1ff !important;   /* светлый фон */
        border: 2px solid #805CD2 !important;   /* фиолетовая рамка */
        border-radius: 8px !important;
        padding: 8px !important;
        color: #000 !important;
        font-weight: 500;
    }
    div[role="radiogroup"] label div:hover {
        transform: scale(1.03);
        border-color: #9448C6 !important;
    }
    div[role="radiogroup"] label div {
        transition: all 0.2s ease-in-out;
    }
    div[role="radiogroup"] label div {
        font-size: 20px !important;
        font-weight: bold !important;
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
    .center-button {
        display: flex;
        justify-content: center;
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
    div[data-testid="stHeader"] > label > div:rc-overflow-item {
        background: #ffffff;
        border-radius: 16px;
        padding: 12px 20px;
        max-width: 100px;
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
# ---------------- AUTHENTIFICATION ----------------
if "user" not in st.session_state:
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Roboto&display=swap" rel="stylesheet">
        <h1 style="
            margin-bottom: -20px;
            font-family: 'Montserrat', 'Roboto', sans-serif;
            margin-top: -10px;
            letter-spacing: -0.5px;
            font-weight: 800;
            font-size: 48px;
            color: #111;
            text-align: center;
        ">
            Login / Register
        </h1>
        """,
        unsafe_allow_html=True,
    )
    mode = st.radio("", ["Login", "Register"], horizontal=True)
    email = st.text_input("**Email:**")
    password = st.text_input("**Password:**", type="password")
    with st.container():
        col = st.columns([2,1,2])[1]
        button_clicked = False
        with col:
            if st.button(mode, use_container_width=True):
                button_clicked = True
        if button_clicked:
            if mode == "Register":
                try:
                    uid = register_user(email, password)
                    result = login_user(email, password)
                    if "idToken" in result:
                        st.session_state["user"] = result
                        st.success("Registred&Logged in!")
                        st.rerun()
                    else:
                        st.error(result.get("error", {}).get("message", "Login failed"))
                except Exception as e:
                    st.error(str(e))
            else:
                result = login_user(email, password)
                if "idToken" in result:
                    st.session_state["user"] = result
                    st.success("Logged in!")
                    st.rerun()
                else:
                    st.markdown("""<div style='text-align: center; color: red; padding: 10px; font-weight: bold;'>Incorrect Email/Password, try again!</div>""",unsafe_allow_html=True)

else:
# ---------------- NAVIGATION ----------------
    pages = {
        "Main": [
            st.Page("pages\quiz_prototype.py", title="Quiz"),
            st.Page("pages\quiz_adaptive_v2.py", title="Premium Quiz"),
            st.Page("pages\profile_prototype.py", title="Profile"),
        ]
    }
    pg = st.navigation(pages,position="top")
    pg.run()
    # ---------------- PAGE CONFIG ----------------
    try:
        im = Image.open(rf"Find_yourself\web_server\logo-round.png")
    except Exception:
        im = None
    st.set_page_config(
        page_title="Find Yourself",
        page_icon=im,
        layout="centered"
    )
