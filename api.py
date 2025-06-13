from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re

app = FastAPI()
model = joblib.load("flood_tweet_model.pkl")  # pastikan file ini ada

class TweetInput(BaseModel):
    text: str

def clean_input(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"@\w+|#", '', text)
    text = re.sub(r"[^a-z\s]", '', text)
    return text

@app.post("/predict")
def predict(input: TweetInput):
    cleaned = clean_input(input.text)
    prediction = model.predict([cleaned])[0]
    prob = model.predict_proba([cleaned]).max()
    return {
        "text": input.text,
        "label": prediction,
        "confidence": f"{prob:.2%}"
    }
