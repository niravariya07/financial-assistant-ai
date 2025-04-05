import streamlit as st

crypto_data = [
        {"name": "Loss", "value": "-45,000"},
    ]


def crypto_status_main():
    st.write("Profit / Loss")
    with st.container():
        cols = st.columns(len(crypto_data))
        for i, stock in enumerate(crypto_data):
            with cols[i]:
                stock_tile = f"""
                <div class="tile">
                    <b>{stock['name']}</b><br>
                    <p>{stock['value']}</p>
                </div>
                """
                st.markdown(stock_tile, unsafe_allow_html=True)

