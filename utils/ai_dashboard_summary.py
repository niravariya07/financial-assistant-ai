from google import genai

def dashboard_summary(stocks_info, crypto_info, user_id):

    crypto_data = crypto_info[crypto_info['u_id'] == user_id]
    stocks_data = stocks_info[stocks_info['u_id'] == user_id]
      
    prompt = f"""
    -greet user
    -Observe stocks and cryptocurrency investment information.
    -analysis that they are in profit or loss.
    -Summarize any significant patterns or anomalies

    Here’s the data I have for this analysis:
    - **Top Stocks**: {stocks_data} 
    - **Top Cryptocurrencies**: {crypto_data} 

    Provide the output like story telling. Keep the output short and precise.
    Don't give any headline.
    """
    client = genai.Client(api_key="AIzaSyCP0iauXrxRHnfHFyqTtcrEvWx1UDiUTYs")
    llm = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return llm.text
