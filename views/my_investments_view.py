import streamlit as st
from components.investments_crypto_info import invested_crypto_info
from components.investments_stocks_info import invested_stocks_info

def my_investments_main(user_name, user_info, crypto_info, crypto_info_csv, stocks_info, stocks_info_csv):    
    
    with st.container(key='investments-container'):
        tab1, tab2 = st.tabs(["Stocks","Crypto"])
    
        with tab1:
            invested_stocks_info(user_name=user_name, user_info=user_info, stocks_info=stocks_info, stocks_info_csv=stocks_info_csv)
        with tab2:
            invested_crypto_info(user_name=user_name, user_info=user_info, crypto_info=crypto_info,crypto_info_csv= crypto_info_csv)
