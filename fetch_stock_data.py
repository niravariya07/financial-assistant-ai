import requests

# Define your Alpha Vantage API Key
API_KEY = 'KXXRIW2SW7HRQ8PZ'  # Replace with your actual API key

# Stock name that you are interested in (e.g., 'AAPL' for Apple)
stock_name = 'AAPL'  # You can change this to any stock symbol you want

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(stock_name):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={API_KEY}'
    
    try:
        # Sending the GET request, with verify=False to bypass SSL verification errors
        response = requests.get(url, verify=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if 'Time Series (Daily)' in data:
                return data['Time Series (Daily)']
            else:
                print(f"Error: {data.get('Note', 'No time series data found.')}")
                return None
        else:
            print(f"Error fetching stock data. Status code: {response.status_code}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching stock data: {e}")
        return None


# Example usage (you can directly run this function without user input)
stock_data = fetch_stock_data(stock_name)

if stock_data:
    print(f"\nTop 5 Days of Stock Data for {stock_name}:\n")
    # Limit to top 5 days of stock data for display
    for idx, (date, data) in enumerate(stock_data.items(), start=1):
        if idx > 5:  # Limit to the first 5 days of data
            break
        print(f"Date: {date}")
        print(f"Open: {data['1. open']}")
        print(f"High: {data['2. high']}")
        print(f"Low: {data['3. low']}")
        print(f"Close: {data['4. close']}")
        print(f"Volume: {data['5. volume']}\n")
else:
    print(f"Failed to fetch stock data for {stock_name}.")
 