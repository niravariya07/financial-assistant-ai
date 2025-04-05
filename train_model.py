import json
import os
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
 
def train_model():
    """
    Trains a logistic regression model using sentiment data and saves it as stock_prediction.pkl.
    """
    input_file = "data/sentiment_data.json"
    model_file = "models/stock_prediction.pkl"
 
    if not os.path.exists(input_file):
        raise FileNotFoundError("❌ sentiment_data.json not found! Run sentiment_analysis.py first.")
 
    # Load the sentiment data
    with open(input_file, "r", encoding="utf-8") as file:
        sentiment_data = json.load(file)
 
    if not sentiment_data:
        raise ValueError("❌ sentiment_data.json is empty!")
 
    X = []
    y = []  # Labels: 1 (Stock Up) or 0 (Stock Down)
 
    # Extract features (sentiment score) and assign labels
    for entry in sentiment_data:
        sentiment_score = entry.get("sentiment_score")  # Fixing the key name
        if sentiment_score is None:
            raise KeyError("❌ 'sentiment_score' key missing in sentiment_data.json")
 
        X.append([sentiment_score])
        y.append(1 if sentiment_score > 0 else 0)  # Stock goes up if sentiment is positive
 
    # Convert to NumPy arrays
    X = np.array(X)
    y = np.array(y)
 
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
    # Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)
 
    # Save the trained model
    os.makedirs("models", exist_ok=True)
    with open(model_file, "wb") as file:
        pickle.dump(model, file)
 
    print("✅ Model trained successfully! Saved to models/stock_prediction.pkl.")
 
# Run training when script is executed
if __name__ == "__main__":
    train_model()