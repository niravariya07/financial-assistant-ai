# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# import os
# from dotenv import load_dotenv

# # Load API keys
# load_dotenv()
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
# def agents_main( ):

#     # st.title(current_language)    
#     # Define Agents
#     web_Search_agent = Agent(
#         name="Web Search Agent",
#         role="Search the web for financial news",
#         model=Groq(id="llama3-70b-8192"),
#         tools=[DuckDuckGo()],
#         instructions=["Always include sources"],
#         show_tools_calls=True,
#         markdown=True,
#     )

#     finance_agent = Agent(
#         name="Finance AI Agent",
#         model=Groq(id="llama3-70b-8192"),
#         tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
#         instructions=["Use tables to display the data"],
#         show_tool_calls=True,
#         markdown=True,
#     )

#     multi_ai_agent = Agent(
#         team=[web_Search_agent, finance_agent],
#         model=Groq(id="llama3-70b-8192"),
#         instructions=["Use the web search agent for company info and the finance agent for stock data."],
#         show_tool_calls=True,
#         markdown=True,
#     )

#     st.title("AI-Powered Financial Assistant")
#     st.subheader("Ask AI Financial Assistant")
#     user_query = st.text_area("Ask about stock trends, investments, or finance!")
#     if st.button("Get Insights"):
#         ai_response = multi_ai_agent.run(user_query)
#         if hasattr(ai_response, 'data'):
#             ai_response = ai_response.data  # Extract actual response content
#         st.subheader("AI Insights")
#         st.write(ai_response)