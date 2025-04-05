
from google import genai
import streamlit as st

def budget_planner_main(username, df,stock_data,crypto_data):

    user_data = df[df["user_name"] == username]
    income = user_data["income"].values[0]
    expense = user_data["expense"].values[0]
    goal = st.text_input("Financial Goals:")
    prompt = f"""
    You are a financial advisor assistant. Your task is to help create a budget plan based on the user's monthly income, essential expenses, and financial goals. 
    You will also suggest an investment strategy to help the user save money toward their financial goal.

    1. **Budget Plan**:
    - Analyze the user’s monthly income and expenses.
    - Consider only user given expense and show how much amount is left.
    - Consider stock data and crypto data of the user.

    2. **Financial Goals**:
    - Understand the user's financial goal.
    - Create a plan to allocate a portion of the leftover towards this goal.
    - Give investment plan in simple and give little explanation about investment flow. 

    3. **Investment Plan**:
    - Based on the user’s goal, suggest simple and practical investment options (e.g., savings account, stock market,invest in crypto, bonds, or retirement accounts).
    - Suggest in which stocks user should invest, how much amount should fix in SIP or FD
    - Provide a strategy that balances risk and reward to achieve the goal within a reasonable time frame.
    - Provide realistic investment plan which could be implemented.

    4. **Suggest options according to goal**
        - Analyse the user goal and suggest some options for that goal.
        
    Here’s the data I have for this user:
    - **Monthly Income**: {income}
    - **Essential Expenses**: {expense} (e.g., Rent: 1500, Utilities: 200, Food: 400)
    - **Financial Goal**: {goal} (e.g., Save for investment)
    - **Stock Data**: {stock_data}
    - **Crpto Data**: {crypto_data}
    take all input in Indian Rupees and not in Dollars
    Please provide a comprehensive budget plan, along with investment advice, that will help the user save money and meet their financial goal.
    Provide output in simple and point wise that should be easy to understand and keep the font of output times new roman
    Don't give output too long, keep it short and precise
    """
    client = genai.Client(api_key="AIzaSyCP0iauXrxRHnfHFyqTtcrEvWx1UDiUTYs")
    llm = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    result=""

    if st.button("Generate"):
        if goal:
            result = llm.text
            st.write(result)
            st.success("generated")

        else:
            st.error("Please provide Goal!")

    return result