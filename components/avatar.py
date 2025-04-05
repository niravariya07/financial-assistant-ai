import streamlit as st
def avatar_main(user_name):
    first_letter = user_name[0]
    with st.container(key='user-avatar'):
        st.title(first_letter.upper())