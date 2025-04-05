import streamlit as st
import pandas as pd
def calculate_stocks_profit_loss(username, df, stocks_info_data_frame):
    user_data = df[df["user_name"] == username]
    if user_data.empty:
        st.error("User not found.")
        return
    user_id = user_data['u_id'].values[0]  
    stocks_data = stocks_info_data_frame[stocks_info_data_frame['u_id'] == user_id]
 
    total_stock_investment = 0
    total_stock_value = 0
    for index, row in stocks_data.iterrows(): 
        total_stock_investment += row['cost_price'] * row['quantity']
        total_stock_value += row['current_price'] * row['quantity']
    if total_stock_investment > 0:
        total_stock_profit_loss = total_stock_value - total_stock_investment
        total_stock_percent = (total_stock_profit_loss / total_stock_investment) * 100
        total_stock_profit_loss = round(total_stock_profit_loss, 2)
        total_stock_percent = round(total_stock_percent, 2)
        if total_stock_profit_loss > 0:
            status = "profit"
        else:
            status = "loss"
        return {
                "status": status,
                "total_stock_percent": total_stock_percent
            }
    else:
        return {"error": "No investment found"}
def calculate_crypto_profit_loss(username, df, crypto_info_data_frame):
    user_data = df[df["user_name"] == username]
    if user_data.empty:
        st.error("User not found.")
        return
    user_id = user_data['u_id'].values[0]  
    crypto_data = crypto_info_data_frame[crypto_info_data_frame['u_id'] == user_id]
    total_crypto_investment = 0
    total_crypto_value = 0
    for index, row in crypto_data.iterrows():
        total_crypto_investment += row['cost_price'] * row['quantity']
        total_crypto_value += row['current_price'] * row['quantity']
 
    if total_crypto_investment > 0:
        total_crypto_profit_loss = total_crypto_value - total_crypto_investment
        total_crypto_percent = (total_crypto_profit_loss / total_crypto_investment) * 100
        total_crypto_profit_loss = round(total_crypto_profit_loss, 2)
        total_crypto_percent = round(total_crypto_percent, 2)

        if total_crypto_profit_loss > 0:
            status = "profit"
        else:
            status = "loss"
        return {
                "status": status,
                "total_crypto_percent": total_crypto_profit_loss
            }
    else:
        st.warning("No crypto investments found.")