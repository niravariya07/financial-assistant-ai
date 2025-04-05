import streamlit as st
def top_performing_stocks_card_main(data):
    rows = 4
    cols = 3
    index = 0
    
    for row in range(rows):
        with st.container():
            columns = st.columns(cols,gap='small')
            for col in range(cols):
                if index < len(data):
                    stock = data[index]
                    with columns[col]:
                        stock_tile = f"""
                        <div class="tile">
                            <p class='title-name'>{stock['symbol']}</p>
                            <p class='title-value'>{stock['price']}</p>
                        </div>
                        """
                        st.markdown(stock_tile, unsafe_allow_html=True)
                    index += 1

