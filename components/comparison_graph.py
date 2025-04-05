import streamlit as st
import pandas as pd

def comparison_graph_generator(data, title, labels, color=['#FF0000', '#0000FF']):
        df = pd.DataFrame(data)
        st.bar_chart(df)
        st.write(title)
        st.write("Comparing the cost and current price of each asset:")
