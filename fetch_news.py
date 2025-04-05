import requests

# Your News API Key (replace with your actual API key)
NEWS_API_KEY = '87a871713ca14ca7af9030857fd703dc'  # Replace with your News API key

# Function to fetch news related to a stock/company
def fetch_news(stock_name):
    url = 'https://newsapi.org/v2/everything'
    
    # Parameters for the API request
    params = {
        'q': stock_name,  # Stock name or company name (e.g., 'AAPL' for Apple)
        'apiKey': NEWS_API_KEY,
        'language': 'en',  # Language of news articles
        'sortBy': 'publishedAt',  # Sort by most recent news
        'pageSize': 5  # Limit to top 5 articles
    }
    
    try:
        # Send GET request to News API
        response = requests.get(url, params=params, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            
            if data['status'] == 'ok' and data['articles']:
                # Return the list of articles directly, including the URL
                return data['articles']
            else:
                print(f"No news articles found for {stock_name}.")
                return []
        else:
            print(f"Failed to fetch news. Status code: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching news: {e}")
        return []
