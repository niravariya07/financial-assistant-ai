from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(news_articles):
    """
    Analyzes the sentiment of the news articles using VADER Sentiment Analysis.
    
    :param news_articles: List of news articles (each article should have a 'description' key).
    :return: List of sentiment scores for each article.
    """
    # Initialize VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    sentiment_scores = []

    # Loop through each article and analyze its sentiment
    for article in news_articles:
        # Extract the description of the article
        description = article.get("description", "")
        
        # Calculate the sentiment score using VADER
        sentiment_score = analyzer.polarity_scores(description)["compound"]
        
        # Store the sentiment score (compound score represents overall sentiment)
        sentiment_scores.append(sentiment_score)

    return sentiment_scores
