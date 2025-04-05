import matplotlib.pyplot as plt
import streamlit as st
def ring_chart_main(status,value):
        if status == 'profit': 
                color = '#23E000'
        else: 
                color = '#FFA500'
        Value = [100-value, value,]
        Colors = ['#8ad07e7a',color,]
        plt.figure(facecolor='#ffff0000')
        plt.pie(Value, colors=Colors,
                autopct=f'{value}', pctdistance=.001,textprops={'color':color, 'fontsize' : 45})
        centre_circle = plt.Circle((0, 0), 0.60, fc='#22201d')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.show()
        st.pyplot(fig)
