import requests
import streamlit as st

def usd_to_inr():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        if 'rates' in data and 'INR' in data['rates']:
            return data['rates']['INR']
        else:
            st.warning("Unable to fetch USD to INR exchange rate.")
            return 82.0   
    except Exception as e:
        st.error(f"Error fetching USD to INR rate: {e}")
        return 82.0