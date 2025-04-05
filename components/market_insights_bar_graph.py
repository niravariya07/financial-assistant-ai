import streamlit as st
import matplotlib.pyplot as plt

def market_bar_graph(data):
    symbols = [item['symbol'] for item in data]
    prices = [item['price'] for item in data]

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_visible(False)  
    ax.bar(symbols, prices, color='skyblue')
    ax.set_xlabel('Symbol', color='white')
    ax.set_ylabel('Price', color='white')
    ax.set_facecolor('none')    
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)