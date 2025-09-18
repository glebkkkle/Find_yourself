# ---------------------- IMPORTS ----------------------
import streamlit as st
from PIL import Image
# ---------------------- PAGE CONFIG ----------------------
im = Image.open("logo-round.png")
st.set_page_config(
    page_title="Find Yourself",
    page_icon=im,
    layout="centered"
)
# ---------------------- PAGE HEADER ----------------------
st.markdown("<h1 style='text-align: center; color: black;'>Your Profile</h1>", unsafe_allow_html=True)

if "profile_result" in st.session_state:
    st.write(st.session_state["profile_result"])
else:
    st.warning("No profile data available yet. Please complete the quiz.")

#st.expander("Hard Skills:", expanded=True)
#st.expander("Soft Skills:", expanded=True)
#st.expander("Overall Profile:", expanded=True)

