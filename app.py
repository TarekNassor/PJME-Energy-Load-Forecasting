from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

from src.features.build_features import create_time_features

# --------------------
# App initialization
# --------------------
app = FastAPI(
    title="PJME Electricity Demand Forecasting API",
    description="Forecast hourly electricity demand using XGBoost",
    version="1.0.0"
)

# --------------------
# Load model
# --------------------
MODEL_PATH = os.getenv("MODEL_PATH", "models/pjme_xgb_model.pkl")
model = joblib.load(MODEL_PATH)

# --------------------
# Input schema
# --------------------
class PredictionInput(BaseModel):
    dayofyear: int
    hour: int
    dayofweek: int
    quarter: int
    month: int
    year: int

# --------------------
# Routes
# --------------------
@app.get("/")
def home():
    return {"status": "PJME Forecasting API is running"}

@app.post("/predict")
def predict(data: PredictionInput):
    # Convert input to DataFrame
    df = pd.DataFrame([data.dict()])

    # Feature engineering
    X = create_time_features(df)

    # Prediction
    prediction = model.predict(X)

    return {
        "predicted_PJME_MW": float(prediction[0])
    }