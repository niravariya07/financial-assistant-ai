import streamlit as st
import matplotlib.pyplot as plt
 
def ring_chart_legend_main(income,expense):
        Value = [income-expense, expense]
        Colors = ['#ffe1c8','#ff7b00',]
        labels = [f'Leftover ({income - expense})', f'Expenses ({expense})']
        plt.figure(facecolor='#ffff0000')
        # plt.figure()
        plt.pie(Value, colors=Colors,labels=labels,
                 autopct=f'Income\n{income}', pctdistance=.001, textprops={'color':'orange','fontsize':12})
        centre_circle = plt.Circle((0, 0), 0.6,fc='#424141')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        legend = fig.legend(labels=labels, loc='center right', fontsize=9, frameon=False, handlelength=1, handleheight=1)
        for text in legend.get_texts():
                text.set_color('orange')

        plt.show()
        st.pyplot(fig)
 
