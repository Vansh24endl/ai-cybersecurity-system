import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI securely
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not found in environment variables")

# Create client
client = MongoClient(MONGO_URI)

# Database & collection
db = client.get_database("cybersecurity_db")
pred_col = db.get_collection("predictions")

print("MongoDB connected securely (mongo.py)")


traffic_collection = db["network_traffic"]
pred_col = db["predictions"]  # <-- define the predictions collection

# 🔥 INSERT DUMMY DATA
sample_data = {
    "protocol": "TCP",
    "src_bytes": 1200,
    "dst_bytes": 450,
    "prediction": "Normal"
}

traffic_collection.insert_one(sample_data)

print("Data inserted successfully")

# Example: insert into predictions using sample_data (provide defaults if missing)
pred_col.insert_one({
    "duration": float(sample_data.get("duration", 0.0)),
    "src_bytes": float(sample_data["src_bytes"]),
    "dst_bytes": float(sample_data["dst_bytes"]),
    "prediction": sample_data.get("prediction", "Unknown")
})
# ...existing code...