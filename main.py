from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re

app = FastAPI()  # ← HARUS ADA

model = joblib.load("flood_tweet_model.pkl")

class TweetInput(BaseModel):
    text: str

@app.post("/predict")
def predict(tweet: TweetInput):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', tweet.text.lower())
    pred = model.predict([cleaned])[0]
    return {"label": pred}
