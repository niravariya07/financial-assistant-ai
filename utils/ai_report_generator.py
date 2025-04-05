import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from google import genai
from components.comparison_graph import comparison_graph_generator

def report_generator_main(username, df, crypto_info_data_frame, stocks_info_data_frame):
    user_data = df[df["user_name"] == username]
   
    if user_data.empty:
        return f"User {username} not found in the database."
   
    income = user_data["income"].values[0]
    expense = user_data["expense"].values[0]
    leftover = user_data['leftover'].values[0]
    user_id = user_data['u_id'].values[0]
   
    user_crypto_data = crypto_info_data_frame[crypto_info_data_frame['u_id'] == user_id]
    user_stocks_data = stocks_info_data_frame[stocks_info_data_frame['u_id'] == user_id]
   
    total_expenses = expense
   
    stock_purchase_values = [q * p  for q, p in zip(user_stocks_data['quantity'], user_stocks_data['price'])]
    stock_current_values = [q * c  for q, c in zip(user_stocks_data['quantity'], user_stocks_data['price'])]
    total_stock_value = sum(stock_current_values)
 

    crypto_purchase_values = [q * p  for q, p in zip(user_crypto_data['quantity'], user_crypto_data['cost_price'])]
    crypto_current_values = [q * c  for q, c in zip(user_crypto_data['quantity'], user_crypto_data['current_price'])]
    total_crypto_value = sum(crypto_current_values)
 
    remaining = income - (total_expenses + total_stock_value + total_crypto_value)
 
    expense_percentage = (total_expenses / income) *  100
    stock_percentage = (total_stock_value / income) *  100
    crypto_percentage = (total_crypto_value / income) *  100
    remaining_percentage = (remaining / income) * 100
 
    # Value = [income-expense, expense]
    # Colors = ['#ffe1c8','#FF0000',]
    # labels = [f'Leftover ({income - expense}INR)', f'Expenses ({expense} INR)']
    # plt.figure(facecolor='#ffff0000', figsize=(4, 4))
    # plt.pie(Value, colors=Colors,labels=labels,
    #             autopct=f'{income}', pctdistance=.001, textprops={'color':'grey','fontsize':10})
    # centre_circle = plt.Circle((0, 0), 0.6,fc='#22201d')
    # fig = plt.gcf()
    # fig.gca().add_artist(centre_circle)        
    # legend = fig.legend(labels=labels, loc='lower left', fontsize=9, frameon=False, handlelength=2, handleheight=1)      
    # for text in legend.get_texts():
    #         text.set_color('white')
    # plt.show()
    # st.pyplot(fig)
 
    
    stocks_data = {
        "Stock Name": user_stocks_data['symbol'].values,
        "Cost Price": user_stocks_data['cost_price'].round(2).values,
        "Current Price": user_stocks_data['price'].round(2).values
    }

    comparison_graph_generator(stocks_data, "Stock Price Comparison", ['Cost Price', 'Current Price'])
 
    crypto_data = {
        "Crypto Name": user_crypto_data['crypto_name'].values,
        "Cost Price": user_crypto_data['cost_price'].round(2).values,
        "Current Price": user_crypto_data['current_price'].round(2).values
    }
    comparison_graph_generator(crypto_data, "Crypto Price Comparison", ['Cost Price', 'Current Price'])
 

    summary = f"""
    Act as an expert financial analyst. Given the user’s financial data below, generate a **detailed financial analysis** with insights, risk assessments, and actionable recommendations.

    ### **User Financial Data:**
    - **Username:** {username}
    - **Monthly Income:** ₹{income:.2f}
    - **Essential Expenses:** ₹{total_expenses:.2f} ({expense_percentage:.2f}% of income)
    - **Stocks Value:** ₹{total_stock_value:.2f} ({stock_percentage:.2f}% of income)
    - **Crypto Holdings:** ₹{total_crypto_value:.2f} ({crypto_percentage:.2f}% of income)
    - **Remaining Savings:** ₹{remaining:.2f} ({remaining_percentage:.2f}% of income)

    ### **Instructions for AI Analysis:**
    1. **Summarize financial health** by comparing income, expenses, and investments.
    2. **Assess risk levels** in the user's stock and crypto portfolio.
    3. **Identify potential budget improvements** to enhance savings.
    4. **Provide portfolio diversification recommendations** for risk balance.
    5. **Offer insights on financial growth strategies** based on the given data.
    6. **Ensure an AI-generated, unique analysis**—do not simply restate values.


    **Overall Financial Summary for {username}:**
    -------------------------------------------------
    - **Income vs Expenses:** Your essential expenses take up **{expense_percentage:.2f}%** of your income, leaving ₹{remaining:.2f} for savings and investments.
    - **Stock & Crypto Holdings:** Your stock investments form **{stock_percentage:.2f}%**, while crypto makes up **{crypto_percentage:.2f}%**, indicating a **moderate/high-risk portfolio**.
    - **Risk Assessment:** Crypto is volatile; consider adjusting allocations for **long-term stability**.

    **Actionable Insights:**
    - **Reduce discretionary spending** by X% to save ₹Y more monthly.
    - **Diversify investments** by allocating X% into stable assets (e.g., bonds, ETFs).
    - **Consider rebalancing** stock vs. crypto to align with risk tolerance.

    **Portfolio & Net Worth Analysis:**

    - **Diversification Check:** Evaluate asset mix for better risk-adjusted returns.
    - **Long-Term Strategy:** Adjust savings and investment contributions for financial security.

    Generate a **clear, insightful, and data-driven** financial report using this structured approach.
        """
    client = genai.Client(api_key="AIzaSyCP0iauXrxRHnfHFyqTtcrEvWx1UDiUTYs")
    llm = client.models.generate_content(model="gemini-2.0-flash", contents=summary)
    st.write(llm.text)
    return llm.text
     