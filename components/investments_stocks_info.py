import streamlit as st
from components.ring_chart import ring_chart_main
from components.side_graph import side_graph_main
from utils.csv_operations import append_to_csv
from utils.data_updator import update_user_data
from utils.exchange_rate_getter import usd_to_inr
from utils.fetchers import fetch_from_yahoo_finance
from utils.ai_dashboard_summary import dashboard_summary



def invested_stocks_info(user_name, user_info, stocks_info, stocks_info_csv): 
                user_data = user_info[user_info["user_name"] == user_name]
                user_id = user_data['u_id'].values[0]
                user_stocks_data = stocks_info[stocks_info['u_id'] == user_id]

                total_stocks_investment = user_data['total_investments_stock']
                total_investment = user_data['total_investments']

                col=st.columns((1,1,1,1), gap='small')
                with col[0]: 
                        st.metric(label='Total invested', value=round(float(total_investment),2))
                        st.title('')
                        st.metric(label='Total investment in stocks', value=round(float(total_stocks_investment),2))
                with col[1]:   
                        with st.container(key="investments-percentages-container"):
                                st.subheader("Investments %")
                                ring_chart_main('loss',60)      
                with col[2]:
                        with st.container(key="profit-loss-container"):
                                st.subheader("Profit/Loss")
                                ring_chart_main('profit',90)



                with col[3]: 
                        with st.container(key="side-graph-stocks"):
                                side_graph_main(path='repo/top_stocks_gainers.csv')


                col=st.columns((1,1), gap="small")
                with col[0]:   
                        with st.container(key='get-stock-value'):
                                stock_name=st.text_input("Get Stocks Value")
                                if st.button("Fetch", key='stock-value-fetcher') :         
                                        if stock_name:
                                                exchange_rate = usd_to_inr()
                                                stock_data = fetch_from_yahoo_finance(stock_name.upper(), exchange_rate)
                                                if stock_data:
                                                        current_price = stock_data['price']
                                                        st.subheader(f"Current Price of {stock_name.upper()} :\n{round(current_price, 2):.2f} INR")  
                with col[1]:
                        with st.container(key='purchase-stock'):
                                stock_name_to_purchase = st.text_input("Stock Name")
                                stock_quantity = st.number_input("Stocks Quantity")
                                if st.button("Purchase Stock",key='update-to-stocks'): 
                                        if stock_name_to_purchase and stock_quantity > 0:
                                                exchange_rate = usd_to_inr()
                                                stock_data = fetch_from_yahoo_finance(stock_name_to_purchase.upper(), exchange_rate)
                                                if stock_data:
                                                        current_price = stock_data['price']
                                                        cost_price = current_price
                                                        new_stock_data = {
                                                        'u_id': user_id,
                                                        'stock_name': stock_name_to_purchase.upper(),
                                                        'cost_price': cost_price,
                                                        'current_price': current_price,
                                                        'quantity': stock_quantity,
                                                        }
                                                        append_to_csv(new_stock_data, stocks_info_csv)
                                                        update_user_data(user_name=user_name)
                                                        st.success(f"{stock_name_to_purchase.upper()} added to your portfolio!")

                with st.container(key="stocks-summary-"):
                        st.subheader("Stocks Summary")
                        st.write(dashboard_summary(stocks_info=user_stocks_data,crypto_info=user_stocks_data, user_id=user_id))
