import json
import pickle
import numpy as np
 
def predict_stock_movement():
    # Load trained model
    with open("models/stock_prediction.pkl", "rb") as file:
        model = pickle.load(file)
 
    # Load sentiment data
    with open("data/sentiment_data.json", "r") as file:
        sentiment_data = json.load(file)
 
    # Extract sentiment scores
    sentiments = [article["sentiment"] for article in sentiment_data]
 
    # Convert to numpy array
    X = np.array(sentiments).reshape(-1, 1)
 
    # Predict stock movement
    predictions = model.predict(X)
    avg_prediction = np.mean(predictions)
 
    result = "⬆ Stock likely to go UP" if avg_prediction > 0.5 else "⬇ Stock likely to go DOWN"
    print(f"Prediction: {result}")
 
if __name__ == "__main__":
    predict_stock_movement()