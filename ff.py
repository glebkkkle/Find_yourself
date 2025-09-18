import streamlit as st

# Check if answers exist
if "submitted_answers" in st.session_state:
    submitted_answers = st.session_state.submitted_answers
    st.write("Here are the submitted answers:")
    st.write(submitted_answers)
else:
    st.warning("No answers submitted yet.")


print(submitted_answers)


f