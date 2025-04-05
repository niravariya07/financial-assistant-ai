import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
def correlation_analysis():
    # Load sentiment data
    with open("data/sentiment_data.json", "r") as file:
        sentiment_data = json.load(file)
 
    # Load stock data
    with open("data/stock_data.json", "r") as file:
        stock_data = json.load(file)
 
    # Extract sentiment scores
    sentiments = [article["sentiment"] for article in sentiment_data]
 
    # Extract stock close prices
    stock_dates = list(stock_data.keys())[:len(sentiments)]
    close_prices = [float(stock_data[date]["4. close"]) for date in stock_dates]
 
    # Create a DataFrame
    df = pd.DataFrame({"Sentiment": sentiments, "Close Price": close_prices})
 
    # Calculate correlation
    correlation = df.corr()
    print("Correlation Matrix:")
    print(correlation)
 
    # Plot correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation between Sentiment and Stock Price")
plt.show()
 
if __name__ == "__main__":
    correlation_analysis()