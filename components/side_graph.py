import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
def side_graph_main(path):
    csv_path = path
    df = pd.read_csv(csv_path)
    df_top12 = df.nlargest(12, 'price')
    fig, ax = plt.subplots(figsize=(8,9.15))  
    df_top12.plot(kind='bar', x='symbol', y='price', ax=ax, color=df['price'].apply(lambda x: 'red' if x < 0 else 'lime'))
    plt.rcParams.update({
        'font.size': 14,
        'text.color': 'white',
        'axes.labelcolor': 'white',
        'axes.titlecolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white'
    })
    ax.set_xlabel("Symbol")
    ax.set_ylabel("Price")
    ax.set_title("Bar Chart of Prices")
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    
    st.pyplot(fig)