import streamlit as st
import pandas as pd
from components.market_insights_bar_graph import market_bar_graph
from components.top_performing_crypto import top_performing_crypto_card_main
from components.top_performing_stocks import top_performing_stocks_card_main
from utils.market_insights_summary import market_insights
from utils.fetchers import top_crypto_fetcher 
from utils.fetchers import top_stock_fetcher



stocks_data = top_stock_fetcher()
crypto_data = top_crypto_fetcher()
summary = market_insights(stock_data=stocks_data,crypto_data=crypto_data)
 
def market_insights_main():
 
    col = st.columns((1,1),gap="small")
    with col[0]:
        with st.container(key='mi-stocks-container', height=520):
            st.subheader("Stocks")
            tab1, tab2 = st.tabs(['Data','Graph'])
            with tab1:
                top_performing_stocks_card_main(stocks_data)
            with tab2:
                market_bar_graph(stocks_data)
    
 
    with col[1]:
        with st.container(key='mi-crypto-container', height=520):
            st.subheader("Crypto")
            tab1, tab2 = st.tabs(['Data','Graph'])
    
            with tab1:
                top_performing_crypto_card_main(crypto_data)
            with tab2:
                market_bar_graph(crypto_data)
    st.subheader("AI Insights")
    with st.container(key='market-insight1'):
        st.subheader("Market Trends")
        st.write(summary['Market Trends'])

    with st.container(key='market-insight2'):
        st.subheader("Investment Opportunities")
        st.write(summary['Investment Opportunities'])

    with st.container(key='market-insight3'):
        st.subheader("Risk Warnings")
        st.write(summary['Risk Warnings'])
        