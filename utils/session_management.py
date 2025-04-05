import streamlit as st
 
def logout():
    st.session_state["logged_in"] = False
    st.session_state["page"] = "home"
    st.rerun()
 
def login():
    st.session_state["logged_in"] = True
    st.session_state["page"] = "dashboard"

