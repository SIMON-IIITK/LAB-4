from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "Wine Quality Inference API"}

@app.post("/predict")
def predict(features: list):
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)[0]

    return {
        "name": "Simon",
        "roll_no": "YOUR_ROLL_NO",
        "wine_quality": int(prediction)
    }
