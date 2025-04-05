import streamlit as st
import joblib
import os
import pandas as pd
from fetch_news import fetch_news
from fetch_stock_data import fetch_stock_data
from sentiment_analysis import analyze_sentiment  # Sentiment analysis function
from train_model import train_model

def news_sentiment_analysis():
    # Set the title of the app
    st.title("📈 News Sentiment Stock Prediction")

    # Input for stock name
    stock_name = st.text_input("Enter Stock Name")

    # Initialize variables to store results
    news_result = None
    stock_result = None
    sentiment_scores = []

    # Section to fetch news and analyze sentiment
    if st.button("Fetch News & Analyze Sentiment"):
        if stock_name:
            # Fetch news related to the stock name
            news_result = fetch_news(stock_name)
            # Fetch stock data related to the stock name
            stock_result = fetch_stock_data(stock_name)

            # Check if the news result has any errors
            if "error" in news_result:
                st.error(news_result["error"])
            else:
                # Perform sentiment analysis (pass the fetched news to analyze_sentiment)
                sentiment_scores = analyze_sentiment(news_result)  # Pass the news_result here
                st.success("News & Sentiment Analysis Done!")

                # Display the latest news with clickable links
                st.subheader(f"Latest News for {stock_name}")
                for article in news_result[:5]:  # Display top 5 articles
                    st.write(f"🔹 **{article['title']}**")
                    st.write(f"📝 {article['description']}")
                    if article['url']:  # Check if the URL exists
                        st.markdown(f"[Read more]({article['url']})")  # Display clickable link
                
                # Display stock data in a table
                if stock_result:
                    st.subheader(f"Stock Data for {stock_name}")
                    # Convert stock data to DataFrame for tabular display
                    stock_df = pd.DataFrame.from_dict(stock_result, orient='index')
                    stock_df.index.name = 'Date'
                    stock_df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
                    st.dataframe(stock_df)

                # Make the prediction automatically after analyzing sentiment
                if sentiment_scores:
                    latest_sentiment_score = sentiment_scores[-1]  # Use the last sentiment score

                    # Predict the stock movement based on the sentiment score
                    model_path = "models/stock_prediction.pkl"
                    if os.path.exists(model_path):
                        model = joblib.load(model_path)
                        prediction = model.predict([[latest_sentiment_score]])

                        # Display the prediction
                        st.subheader(f"📊 Prediction for {stock_name}: {'📈 Up' if prediction[0] == 1 else '📉 Down'}")
                    else:
                        st.error("Model not trained yet!")
        else:
            st.warning("Please enter a stock name.")
