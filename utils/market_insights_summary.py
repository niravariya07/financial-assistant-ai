import streamlit as st
from google import genai
import pandas as pd
import json
 
# Read the CSV file
# stock_csv = '../data/stock_gainers 1.csv'
# crypto_csv = '../data/crypto_gainers 1.csv'
# user_stock_csv = '../data/stocks_info.csv'
# user_crypto_csv = '../data/crypto_info.csv'
# user_stock_data=pd.read_csv(user_stock_csv)
# user_crypto_data = pd.read_csv(user_crypto_csv)
# stock_data = pd.read_csv(stock_csv)
# crypto_data = pd.read_csv(crypto_csv)
 
def market_insights(stock_data, crypto_data):
    prompt = f"""
    You are a financial advisor assistant. Your task is to provide market insights based on data for top stocks and cryptocurrencies.
    1. **Market Trends**:
    - Analyze the current trends in the stock and cryptocurrency markets.
    - Highlight significant movements, patterns, or shifts observed in the market.
 
    2. **Investment Opportunities**:
    - Identify potential investment opportunities based on the current market data.
    - Explain why these stocks or cryptocurrencies are promising and what factors contribute to their potential growth.
 
    3. **Risk Warnings**:
    - Provide a detailed risk assessment for the identified investment opportunities.
    - Discuss any potential risks or uncertainties that investors should be aware of before making investment decisions.
 
    Here’s the data I have for this analysis:
    - **Top Stocks**: {stock_data} (e.g., Tesla (TSLA), Apple (AAPL), Amazon (AMZN))
    - **Top Cryptocurrencies**: {crypto_data} (e.g., Bitcoin (BTC), Ethereum (ETH), Tether (USDT))
 
    Provide the output in a simple, point-wise format that is easy to understand. Keep the output short and precise.
    Don't give any headline.
 
    Give the output in the following format:
    {{
        "Market Trends": "Information about market trends",
        "Investment Opportunities": "Information about investment opportunities",
        "Risk Warnings": "Information about risk warnings"
    }}
    """
    client = genai.Client(api_key="AIzaSyCP0iauXrxRHnfHFyqTtcrEvWx1UDiUTYs")
    llm = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    response_text = llm.text.strip().strip('```json').strip('```').replace('\\', ' ')
 
    try:
        output = json.loads(response_text)
    except json.JSONDecodeError as e:
        st.error(f"Failed to decode JSON: {e}")
        st.error(f"Response from model: {response_text}")
        return None
 
    return output
