import requests
import yfinance as yf
import streamlit as st

def fetch_from_yahoo_finance(symbol, exchange_rate, period="7d"):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)   
        if not data.empty:
            # Convert to INR
            data['Close INR'] = data['Close'] * exchange_rate
            return {
                'symbol': symbol,
                'price': data['Close INR'].iloc[-1],
                'history': data[['Close INR']]
            }
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {e}")
        return None

def top_crypto_fetcher():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'percent_change_24h',
        'per_page': 12,
        'page': 1
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data:
            return [{"symbol": coin['symbol'].upper(), "name": coin['name'], "price": coin['current_price']} for coin in data]
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching top crypto gainers: {e}")
        return None
 
def top_stock_fetcher():
    url = "https://financialmodelingprep.com/api/v3/stock_market/gainers"
    params = {
        'apikey': 'XaYhYWPBrzUc0nEVHcJNs6PAPaKFn3S3'
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
 
        if data:
            top_gainers = []
            for stock in data[:12]:
                # Ensure 'name' field exists in the stock data
                symbol = stock.get('symbol')
                name = stock.get('name', 'Unknown')  # Default to 'Unknown' if 'name' is missing
                price = stock.get('price', 0)
                
                if symbol and price:
                    top_gainers.append({"symbol": symbol, "name": name, "price": price})
            
            return top_gainers
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching top stock gainers from FMP: {e}")
        return None
 
def fetch_crypto_data(symbol, exchange_rate):
    """
    Fetch cryptocurrency data from Yahoo Finance
    """
    try:
        # Make sure symbol has `-USD` format like BTC-USD, ETH-USD
        if '-' not in symbol:
            #st.error("Please enter a valid crypto symbol with USD suffix, e.g., BTC-USD")
            return None
 
        # Fetch data from Yahoo Finance (for cryptocurrencies)
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")  # Fetch latest 1-day data
 
        if not data.empty:
            # Convert to INR if needed (you can add logic for exchange rates if necessary)
            data['Close INR'] = data['Close'] * exchange_rate
            return {
                'symbol': symbol,
                'price': data['Close INR'].iloc[-1],
                'history': data[['Close INR']]
            }
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data for crypto {symbol}: {e}")
        return None