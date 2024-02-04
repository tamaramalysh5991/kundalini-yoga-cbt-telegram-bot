from pymongo import MongoClient


client = MongoClient("mongodb://mongodb:27017/")
db = client["telegram_bot_db"]
user_collection = db["users"]
