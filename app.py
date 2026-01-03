import os
import joblib
import numpy as np
from flask import Flask, render_template, request
from pymongo import MongoClient

# ---------------- APP SETUP ----------------
app = Flask(__name__)

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

print("Loading model from:", MODEL_PATH)
model = joblib.load(MODEL_PATH)
print("Model loaded successfully")
print("Model expects features:", model.n_features_in_)

# ---------------- MONGODB ----------------
client = MongoClient("mongodb+srv://vansh_20:sheetal@cluster0.nblowqv.mongodb.net/?appName=Cluster0")
db = client["cybersecurity_db"]
pred_col = db["predictions"]

print("MongoDB connected")

# ---------------- HOME ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            duration = float(request.form.get("duration"))
            src_bytes = float(request.form.get("src_bytes"))
            dst_bytes = float(request.form.get("dst_bytes"))

            print("Input received:", duration, src_bytes, dst_bytes)

            # -------- FEATURE ALIGNMENT --------
            input_vector = np.zeros((1, model.n_features_in_))
            input_vector[0][0] = duration
            input_vector[0][1] = src_bytes
            input_vector[0][2] = dst_bytes

            # -------- ML PREDICTION --------
            raw_pred = model.predict(input_vector)[0]
            pred_int = int(raw_pred)

            if pred_int == 1:
                prediction = "Attack"
            else:
                prediction = "Normal"

            # -------- HYBRID SECURITY RULE --------
            if duration > 3000 and src_bytes > 50000:
                prediction = "Attack (Rule-Based)"

            print("Final Prediction:", prediction)

            # -------- SAVE TO DB --------
            pred_col.insert_one({
                "duration": float(duration),
                "src_bytes": float(src_bytes),
                "dst_bytes": float(dst_bytes),
                "prediction": prediction
            })

            if "Attack" in prediction:
                print("🚨 ALERT: Possible Intrusion Detected!")

        except Exception as e:
            error = str(e)
            print("ERROR:", error)

    return render_template("index.html", prediction=prediction, error=error)


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    records = list(
        pred_col.find({}, {"_id": 0})
                .sort([("_id", -1)])
                .limit(20)
    )

    normal_count = pred_col.count_documents({"prediction": {"$regex": "Normal"}})
    attack_count = pred_col.count_documents({"prediction": {"$regex": "Attack"}})

    return render_template(
        "dashboard.html",
        records=records,
        normal_count=normal_count,
        attack_count=attack_count
    )


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
