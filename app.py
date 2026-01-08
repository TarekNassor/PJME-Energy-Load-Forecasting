from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("pjme_xgb_model.pkl")

app = FastAPI(
    title="PJME Electricity Demand Forecasting API",
    description="Forecast hourly electricity demand using XGBoost",
    version="1.0"
)

# Input schema
class PredictionInput(BaseModel):
    dayofyear: int
    hour: int
    dayofweek: int
    quarter: int
    month: int
    year: int

@app.get("/")
def home():
    return {"message": "PJME Forecasting API is running"}

@app.post("/predict")
def predict(data: PredictionInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)

    return {
        "predicted_PJME_MW": float(prediction[0])
    }
