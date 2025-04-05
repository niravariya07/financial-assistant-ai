import streamlit as st
def global_page_style(css_path):
    
    with open(css_path) as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

