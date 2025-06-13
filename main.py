from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import re

# Init
app = FastAPI()
templates = Jinja2Templates(directory="templates")
model = joblib.load("flood_tweet_model.pkl")

# Util
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"@\w+|#", '', text)
    text = re.sub(r"[^a-z\s]", '', text.lower())
    return text.strip()

# =========================
# 🔘 FORM HTML INTERFACE
# =========================
@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
def handle_form(request: Request, tweet: str = Form(...)):
    cleaned = clean_text(tweet)
    pred = model.predict([cleaned])[0]
    probas = model.predict_proba([cleaned])[0]
    confidence = round(probas[list(model.classes_).index(pred)] * 100, 2)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "tweet": tweet,
        "result": pred,
        "confidence": confidence
    })

# =========================
# 🔌 API JSON ENDPOINT
# =========================
class TweetInput(BaseModel):
    text: str

@app.post("/predict")
def predict_api(data: TweetInput):
    cleaned = clean_text(data.text)
    pred = model.predict([cleaned])[0]
    probas = model.predict_proba([cleaned])[0]
    confidence = round(probas[list(model.classes_).index(pred)] * 100, 2)

    return {
        "text": data.text,
        "prediction": pred,
        "confidence": f"{confidence} %"
    }
