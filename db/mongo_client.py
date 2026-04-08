from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI)
    db = client["inventoryDB"]
    collection = db["products"]
    print("MongoDB connected successfully ✅")
except Exception as e:
    print("MongoDB connection failed ❌", e)