import streamlit as st 
from components.ring_chart import ring_chart_main
from components.side_graph import side_graph_main
from utils.ai_dashboard_summary import dashboard_summary
from utils.csv_operations import append_to_csv
from utils.exchange_rate_getter import usd_to_inr
from utils.fetchers import fetch_from_yahoo_finance

from utils.profit_loss_management import calculate_crypto_profit_loss 

crypto_data = [
        {"name": "Loss", "value": "-45,000"},
    ]






def invested_crypto_info(user_name, user_info, crypto_info,crypto_info_csv):
                
                

                user_data = user_info[user_info["user_name"] == user_name]
                user_id = user_data['u_id'].values[0]
                
                user_crypto_data = crypto_info[crypto_info['u_id'] == user_id]
                total_crypto_investment = user_data['total_investments_crypto']
                total_investment = user_data['total_investments']

                crypto_data = calculate_crypto_profit_loss(username=user_name,df=user_info, crypto_info_data_frame=crypto_info)

                # st.title(f'{crypto_data}')

                col=st.columns((1,1,1,1), gap='small')
                with col[0]: 
                        st.metric(label='Total invested', value=round(float(total_investment),2))
                        st.title('')
                        st.metric(label='Total investments in crypto', value=round(float(total_crypto_investment),2))
                with col[1]:   
                        with st.container(key="investments-crypto-percentages-container"):
                                st.subheader("Investments %")
                                ring_chart_main('loss',60)      
                with col[2]:
                        with st.container(key="profit-loss-container-crypto"):
                                st.subheader("Profit/Loss")
                                ring_chart_main(status=crypto_data['status'],value=crypto_data['total_crypto_percent'])
                
                with col[3]: 
                        with st.container(key="side-graph-crypto"):
                                side_graph_main(path='repo/top_crypto_gainers.csv')

                col=st.columns((1,1), gap="small")
                with col[0]:   
                        with st.container(key='get-crypto-value'):
                                crypto_name = st.text_input("Get crypto Value")
                                if st.button("Fetch", key='crypto-value-fetcher'): 
                                        if crypto_name: 
                                                exchange_rate = usd_to_inr()
                                                stock_data = fetch_from_yahoo_finance(crypto_name.upper(), exchange_rate)
                                                if stock_data:
                                                        current_price = stock_data['price']
                                                        st.subheader(f"Current Price of {crypto_name.upper()} :\n{round(current_price, 2):.2f} INR")

                with col[1]:

                        with st.container(key='purchase-crypto'):
                                crypto_to_purchase = st.text_input("crypto Name")
                                crypto_quantity = st.number_input("crypto Quantity")
                                if st.button("Purchase Crypto", key='update-to-crypto'):
                                        if crypto_to_purchase and crypto_quantity > 0:
                                                exchange_rate = usd_to_inr()
                                                crypto_data = fetch_from_yahoo_finance(crypto_to_purchase.upper(), exchange_rate)
                                                if crypto_data:
                                                        current_price = crypto_data['price']
                                                        cost_price = current_price
                                                        new_crypto_data = {
                                                                'u_id': user_id,
                                                                'crypto_name': crypto_to_purchase.upper(),
                                                                'cost_price': cost_price,
                                                                'current_price': cost_price,
                                                                'quantity': crypto_quantity,
                                                        }
                                                        append_to_csv(new_crypto_data, crypto_info_csv)
                                                        st.success(f"{crypto_name.upper()} added to your portfolio!")

        

                with st.container(key="crypto-summary-"):
                        st.subheader("Crypto Summary")
                        st.write(dashboard_summary(stocks_info=user_crypto_data,crypto_info=user_crypto_data, user_id=user_id))