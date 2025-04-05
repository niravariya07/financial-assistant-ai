from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import pandas as pd
from views.market_insights_view import market_insights_main
from views.my_investments_view import my_investments_main
from views.dash_view import dash_main
from components.avatar import avatar_main
from utils.ai_budget_planner import budget_planner_main
from utils.ai_report_generator import report_generator_main
from utils.agents import agents_main
from utils.session_management import logout
from views.news import news_sentiment_analysis


def side_navbar_main(user_name, user_id, user_info, crypto_info, crypto_info_csv, stocks_info, stocks_info_csv, user_info_csv):


    col = st.columns((1,1,.3))
    with col[0]:
         st.title("AI Financial Assistant")
    with col[2]:
        current_language = st.selectbox(options=['ENG','FR','HINDI'], label='Language')
        st.session_state['current_language'] = current_language
    
    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Dashboard', 'Investments', 'Market Insights','Budget Planner','Report Generation','News Sentiment Analysis','Agents','Log out'],iconName=['dashboard', 'attach_money', 'data_thresholding','edit_document','summarize','newspaper','support-agent','logout'], default_choice=0)
 
    if tabs =='Dashboard':
        dash_main(user_info=user_info, user_name=user_name, crypto_info=crypto_info, stocks_info=stocks_info, user_id=user_id, user_info_csv = user_info_csv)
        
    elif tabs == 'Investments':
        my_investments_main(user_info=user_info, user_name=user_name, crypto_info=crypto_info, crypto_info_csv=crypto_info_csv, stocks_info=stocks_info, stocks_info_csv=stocks_info_csv)

    elif tabs == 'Market Insights':
        market_insights_main()

    elif tabs == 'Report Generation':
        if st.button(label='generate report'): 
                    st.subheader("Overall Financial Report")
                    report_generator_main(username=user_name,df=user_info,crypto_info_data_frame=crypto_info,stocks_info_data_frame=stocks_info)

                    st.success("Generated")

    elif tabs == 'Budget Planner':
        budget_planner_main(username=user_name,stock_data=stocks_info, crypto_data=crypto_info, df=user_info)
        

    elif tabs == 'Agents':
         agents_main( )
    
    elif tabs == 'News Sentiment Analysis':
         news_sentiment_analysis()

    elif tabs == 'Logout':
        logout()
        st.rerun()
        

 