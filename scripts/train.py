import os
import json
import joblib
import urllib.request
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# ===== MODEL CONFIG =====
CONFIG = {
    "scaling": False,
    "alpha": 1.0,
    "n_estimators": 100,
    "max_depth": 15
}

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
DATA_PATH = "dataset/winequality.csv"

# Create folders
os.makedirs("dataset", exist_ok=True)
os.makedirs("model", exist_ok=True)

# Download dataset
if not os.path.exists(DATA_PATH):
    urllib.request.urlretrieve(DATA_URL, DATA_PATH)

# Load data
data = pd.read_csv(DATA_PATH, sep=";")

X = data.drop("quality", axis=1)
y = (data["quality"] >= 6).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=CONFIG["n_estimators"],
    max_depth=CONFIG["max_depth"],
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)

# Save outputs
joblib.dump(model, "model/model.pkl")

with open("metrics.json", "w") as f:
    json.dump({"f1_score": f1, "config": CONFIG}, f, indent=4)

print("Training completed successfully")
