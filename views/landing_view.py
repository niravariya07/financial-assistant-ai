import streamlit as st
from repo.users_auth_data import users
from utils.data_updator import fetch_current_crypto_price, fetch_current_stocks_price, update_user_data
from utils.session_management import login 
from components.side_navbar import side_navbar_main
import pandas as pd



# INIT

# Files
user_info_csv = "repo/users_info.csv"
crypto_info_csv = 'repo/users_crypto_info.csv'
stocks_info_csv = 'repo/users_stocks_info.csv'


# Dataframes
user_info = pd.read_csv(user_info_csv)
crypto_info = pd.read_csv(crypto_info_csv)
stocks_info = pd.read_csv(stocks_info_csv)
 


# user_name=' '
user_id = 0

def home():
    with st.container(key='hero-title'):
        st.title('Get most out of your money and investments with the power of AI!')    
        # with st.container(key='hero-btns'):
        #     st.button('Learn more', key='learn-more-btn')
        #     st.button('Get Started', key='get-started-btn')
 
        with st.container(key="hero-cards"):
            with st.container(key='info-card1'):
                st.subheader("Investments")
                st.image(r"public/assets/images/investment.png")
                st.write("Be Investment Ready")
                           
            with st.container(key='info-card2'):
                st.subheader("Market Insights")
                st.image(r"public/assets/images/market_insights.png")
                st.write("Get Market Insights")
           
            with st.container(key='info-card3'):
                st.subheader("Tracker")
                st.image(r"public/assets/images/tracker.png")
                st.write("Track your investment goals")
           
            with st.container(key='info-card4'):
                st.subheader("Portfolio")
                st.image(r"public/assets/images/portfolio.png")
                st.write("Build your financial portfolio")
 
def features():
    with st.container(key='hero-features'):
        with st.container(key='feat-card1'):
            st.subheader("Portfolio Management")
            st.image(r"public/assets/images/portfolio_features.png")
            st.write("Tracks stocks, crypto, and investments, offering insights and suggestions.")
       
        with st.container(key='feat-card2'):
            st.subheader("Real-time Market Analysis")
            st.image(r"public/assets/images/market_features.png")
            st.write("Uses APIs (Yahoo Finance, Alpha Vantage, Bloomberg) to fetch real-time stock data.")
       
        with st.container(key='feat-card3'):
            st.subheader("Personalized Financial Advice")
            st.image(r"public/assets/images/financial_advice.png")
            st.write("Uses an LLM-based agent to suggest investments based on user goals.")
       
        with st.container(key='feat-card4'):
            st.subheader("Budget Planning & Expense Tracking")
            st.image(r"public/assets/images/budget_planning.png")
            st.write("Helps users set financial goals and monitor spending.\n")
       
        with st.container(key='feat-card5'):
            st.subheader("Risk Assessment & Alerts")
            st.image(r"public/assets/images/risk_alerts.png")
            st.write("Uses AI models to predict market risks and suggest optimizations.")
       
        with st.container(key='feat-card6'):
            st.subheader("Automated Report Generation")
            st.image(r"public/assets/images/report_generation.png")
            st.write("Generates financial summaries, tax reports, and insights.")
       
        with st.container(key='feat-card7'):
            st.subheader("News Sentiment Analysis")
            st.image(r"public/assets/images/sentiment_analysis.png")
            st.write("Extracts financial news sentiment to predict potential market movements.")
       
        with st.container(key='feat-card8'):
            st.subheader("Conversational Interface")
            st.image(r"public/assets/images/conversational_interface.png")
            st.write("Provides a chatbot (voice/text) for easy interaction.\n")
       
        with st.container(key='feat-card9'):
            st.subheader("Multilingual Support")
            st.image(r"public/assets/images/translator.png")
            st.write("Supports multiple languages for global reach.\n")
 
 
def login_section():
    with st.container(key='login-panel'):
        col = st.columns((1,1))
        with col[0]:
            with st.container(key='login-form'):
                st.title("Login")
                st.write('Please login to continue!')
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.button("Login", key='login-btn'):
                    if username in users and users[username] == password:
                        login()
                        st.session_state["username"] = username
                        global user_id    
                        user_name = st.session_state["username"]
                        
                        


                        user_data = user_info[user_info["user_name"] == user_name]
                        user_id = user_data['u_id'].values[0]

                        fetch_current_stocks_price(stocks_info=stocks_info, stocks_info_csv=stocks_info_csv)
                        st.success("Updating crypto info!")
                        fetch_current_crypto_price(crypto_info=crypto_info, crypto_info_csv=crypto_info_csv)
                        
                        st.success("Updating stocks info!")
                        update_user_data(user_name=user_name)

                        # print('///////////////////Login//////////////////////// after update')

                        st.success("Login successful!")         
                        st.rerun()
                    else:
                        st.error("Invalid username or password. Please try again.")
 
        with col[1]:
            with st.container(key='login-img'):
                st.image("public/assets/images/login_bg_color.png")

def landing_main():
    if not st.session_state.get("logged_in", False):
        with st.container(key='navbar-main'):
            with st.container(key='logo'):
                st.button("FA")
 
            with st.container(key='navbar-btns'):
                if st.button("Home"):
                    st.session_state.page = "home"
                if st.button("Features"):
                    st.session_state.page = "features"
                if st.button("Login"):
                    st.session_state.page = "login"


 
    with st.container(key='hero-section'):
        if "page" in st.session_state:
            if st.session_state.page == "home":
                home()
            elif st.session_state.page == "features":
                features()
            elif st.session_state.page == "login":
                login_section()
            elif st.session_state.page == "dashboard":
                side_navbar_main(user_name=st.session_state.username, user_id = user_id, user_info = user_info,crypto_info = crypto_info,  crypto_info_csv = crypto_info_csv, stocks_info = stocks_info, stocks_info_csv = stocks_info_csv, user_info_csv=user_info_csv  )

 
                """
                    # Files
                    user_info_csv = "repo/users_info.csv"
                    crypto_info_csv = 'repo/users_crypto_info.csv'
                    stocks_info_csv = 'repo/users_stocks_info.csv'
                    top_stocks_csv = 'repo/top_stocks_gainers.csv'
                    top_crypto_csv = 'repo/top_crypto_gainers.csv'

                    # Dataframes
                    user_info = pd.read_csv(user_info_csv)
                    crypto_info = pd.read_csv(crypto_info_csv)
                    stocks_info = pd.read_csv(stocks_info_csv)
                    top_crypto = pd.read_csv(top_crypto_csv)
                    top_stocks = pd.read_csv(top_stocks_csv)
                """
        else:
            home()
