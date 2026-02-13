from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model/model.pkl")

class WineInput(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Wine Quality Inference API"}

@app.post("/predict")
def predict(data: WineInput):
    arr = np.array(data.features).reshape(1, -1)
    prediction = model.predict(arr)[0]

    return {
        "name": "Simon",
        "roll_no": "YOUR_ROLL_NO",
        "wine_quality": int(prediction)
    }
