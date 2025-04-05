import streamlit as st
stocks_data = [
        {"name": "Profit", "value": "+11,100"},
        ]
def stocks_status_main():   
    st.write("Profit / Loss")
    with st.container():
        cols = st.columns(len(stocks_data))  #  
        for i, stock in enumerate(stocks_data):
            with cols[i]:
                stock_tile = f"""
                <div class="tile">
                    <b>{stock['name']}</b><br>
                    <p>{stock['value']}</p>
                </div>
                """
                st.markdown(stock_tile, unsafe_allow_html=True)