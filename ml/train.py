import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from pymongo import MongoClient

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed_train.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "ids_model.pkl")

# ---------- LOAD DATA ----------
df = pd.read_csv(DATA_PATH)

X = df.drop("label", axis=1)
y = df["label"]

# ---------- TRAIN TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------- MODEL ----------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ---------- PREDICTION ----------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n✅ Model Accuracy:", accuracy)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# ---------- SAVE MODEL ----------
os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("\n💾 Model saved at:", MODEL_PATH)

# ---------- MONGODB STORE ----------
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cybersecurity_db"]
    results_col = db["ml_results"]

    result = {
        "model": "Random Forest",
        "accuracy": float(accuracy),
        "features_used": list(X.columns)
    }

    results_col.insert_one(result)
    print("📦 Result saved to MongoDB")

except Exception as e:
    print("⚠ MongoDB not running. Skipping DB save.")

