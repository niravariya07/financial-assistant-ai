import pandas as pd
from utils.fetchers import fetch_from_yahoo_finance
from utils.exchange_rate_getter import usd_to_inr
from utils.csv_operations import update_csv

user_info_csv_path = 'repo/users_info.csv'

def update_live_prices_and_investments(username,user_info, crypto_info, stocks_info, crypto_info_csv, stocks_info_csv):

    # Fetch user data and user_id
    user_data = user_info[user_info["user_name"] == username]
    user_id = user_data['u_id'].values[0]

    total_crypto_investment = 0
    total_stock_investment = 0

    # Update cryptocurrency prices and calculate total investment
    user_crypto_data = crypto_info[crypto_info['u_id'] == user_id]
    if not user_crypto_data.empty:
        for index, row in user_crypto_data.iterrows():
            crypto_name = row['crypto_name']
            updated_crypto = fetch_from_yahoo_finance(crypto_name, usd_to_inr())  # Fetch updated price
            if updated_crypto:
                current_price = updated_crypto['price']
                crypto_info.loc[(crypto_info['u_id'] == user_id) & (crypto_info['crypto_name'] == crypto_name), 'current_price'] = current_price
                total_crypto_investment += row['cost_price'] * row['quantity']

    # Update stock prices and calculate total investment

    user_stocks_data = stocks_info[stocks_info['u_id'] == user_id]
    
    if not user_stocks_data.empty:
        for index, row in user_stocks_data.iterrows():
            stock_name = row['stock_name']
            updated_stock = fetch_from_yahoo_finance(stock_name, usd_to_inr())  # Fetch updated price
            if updated_stock:
                current_price = updated_stock['price']
                stocks_info.loc[(stocks_info['u_id'] == user_id) & (stocks_info['stock_name'] == stock_name), 'current_price'] = current_price
                total_stock_investment += row['cost_price'] * row['quantity']
    
    # Calculate the total investments (crypto + stocks)
    total_investments = total_crypto_investment + total_stock_investment

    # Update the user data with the total investments
    user_info.loc[user_info["user_name"] == username, "total_investments_crypto"] = total_crypto_investment
    user_info.loc[user_info["user_name"] == username, "total_investments_stock"] = total_stock_investment
    user_info.loc[user_info["user_name"] == username, "total_investments"] = total_investments

    # Save updated data to CSV
    crypto_info.to_csv(crypto_info_csv, index=False)
    stocks_info.to_csv(stocks_info_csv, index=False)
    update_csv(user_info, user_info_csv_path)  # Save updated user information

    return total_crypto_investment, total_stock_investment, total_investments



def fetch_current_stocks_price(stocks_info,stocks_info_csv):
    stocks_array = stocks_info['symbol'].to_list()
    stocks_set = set(stocks_array)
    stocks_dict = {item: 0 for item in stocks_set}
    for key in stocks_dict:
        stocks_dict[key] = float(fetch_from_yahoo_finance(symbol=key, exchange_rate=usd_to_inr())['price'])

    df = pd.read_csv(stocks_info_csv)
    df['price'] = df['symbol'].map(stocks_dict)
    df.to_csv(stocks_info_csv, index=False)



def fetch_current_crypto_price(crypto_info, crypto_info_csv):
    crypto_array = crypto_info['crypto_name'].to_list()
    crypto_set = set(crypto_array)
    crypto_dict = {item: 0 for item in crypto_set}
    for key in crypto_dict:
        crypto_dict[key] = float(fetch_from_yahoo_finance(symbol=key, exchange_rate=usd_to_inr())['price'])
    df = pd.read_csv(crypto_info_csv)
    df['current_price'] = df['crypto_name'].map(crypto_dict)
    df.to_csv(crypto_info_csv, index=False)




def update_user_data(user_name):
    user_info_csv = "repo/users_info.csv"
    crypto_info_csv = 'repo/users_crypto_info.csv'
    stocks_info_csv = 'repo/users_stocks_info.csv'
    user_info = pd.read_csv(user_info_csv)
    crypto_info = pd.read_csv(crypto_info_csv)
    stocks_info = pd.read_csv(stocks_info_csv)
    user_data = user_info[user_info["user_name"] == user_name]
    user_id = user_data['u_id'].values[0]
    total_investments=user_data['total_investments'].values[0]
    user_crypto_data = crypto_info[crypto_info['u_id'] == user_id]
    user_stocks_data = stocks_info[stocks_info['u_id'] == user_id]
    total_invested_in_stocks = (user_stocks_data['cost_price'] * user_stocks_data['quantity']).sum()
    total_invested_in_crypto = (user_crypto_data['cost_price'] * user_crypto_data['quantity']).sum()
    total_investments = total_invested_in_crypto + total_invested_in_stocks
    user_info.loc[user_info["user_name"] == user_name, "total_investments"] = total_investments
    user_info.loc[user_info["user_name"] == user_name, "total_investments_crypto"] = total_invested_in_crypto
    user_info.loc[user_info["user_name"] == user_name, "total_investments_stock"] = total_invested_in_stocks
    update_csv(user_info, user_info_csv)