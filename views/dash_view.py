import streamlit as st 
from components.ring_chart_legend import ring_chart_legend_main
from components.side_graph import side_graph_main
from utils.ai_dashboard_summary import dashboard_summary
from utils.csv_operations import update_csv
from utils.translator import translate

def dash_main(user_name,user_info, crypto_info, stocks_info, user_id, user_info_csv):

    


    user_data = user_info[user_info["user_name"] == user_name]
    income = user_data["income"].values[0]
    expense = user_data["expense"].values[0]
    leftover = user_data['leftover'].values[0]
    total_investments=user_data['total_investments'].values[0]

    summary =dashboard_summary(stocks_info=stocks_info, crypto_info=crypto_info, user_id=user_id)
    

    col = st.columns((3,1), gap='small')
    with col[0]:
        with st.container(key='greetings-section'):
            st.metric(label=f"{translate(text='Hello',lang=st.session_state.current_language)}",value=user_name.title())
            st.metric(label=f"{translate(text='Income',lang=st.session_state.current_language)}",value=f"₹ {income}")
            st.metric(label=f"{translate(text='Expense',lang=st.session_state.current_language)}",value=f"₹ {expense}")
            st.metric(label=f"{translate(text='Leftover',lang=st.session_state.current_language)}",value=f"₹ {leftover}")
            st.metric(label=f"{translate(text='Total Investments',lang=st.session_state.current_language)}", value=f"₹ {total_investments}")


        with st.container(key='dashboard-card'):
            
            with st.container(key='ring-chart-section'  ):
                with st.container(key='leftover-expense-chart'):
                    ring_chart_legend_main(expense=expense, income=income)

                with st.container(key='val-updater'):
                    with st.container(key='income-updater'):
                        new_income = st.number_input("Update Income")
                        if st.button("Add Income", key='update-income-button'): 
                                    user_info.loc[user_info["user_name"] == user_name, "income"] += new_income
                                    user_info["leftover"] = user_info["income"] - user_info["expense"]
                                    update_csv(user_info, user_info_csv)
                                    st.success("Data updated successfully!")
                                    st.rerun()

                    with st.container(key='expense-updater'):
                        new_expense = st.number_input("Update Expense")
                        if st.button("Add Expense",key='update-expense-button') : 
                            if new_expense > leftover:
                                st.error("Adding this expense will make your leftover negative. Please adjust the amount.")
                            else:
                                user_info.loc[user_info["user_name"] == user_name, "expense"] += new_expense
                                user_info["leftover"] = user_info["income"] - user_info["expense"]
                                update_csv(user_info, user_info_csv)
                                st.success("Data updated successfully!")
                                st.rerun()
                       
        with st.container(key="summary-container"):
            st.subheader("Summary")
            st.write(summary)
         
    # SIDE GRAPH
    with col[1]:
        with st.container( key='stocks-chart'): 
            st.subheader("Stocks")
            tab1, tab2 = st.tabs(['Your stocks','Top stocks'])
            with tab1:
                side_graph_main("repo/top_stocks_gainers.csv")
            with tab2:
                side_graph_main("repo/top_stocks_gainers.csv")

        with st.container(key='crypto-chart'): 
            st.subheader("Crypto")
            tab1, tab2 = st.tabs(['Your Crypto','Top Crypto'])
            with tab1:
                side_graph_main("repo/top_stocks_gainers.csv")
            with tab2:
                side_graph_main("repo/top_stocks_gainers.csv")
 

 