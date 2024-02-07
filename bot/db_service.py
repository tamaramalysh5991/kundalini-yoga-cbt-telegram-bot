from pymongo import MongoClient
from .config import Config

client = MongoClient(
    Config.MONGODB_URI,
    username=Config.MONGO_INITDB_ROOT_USERNAME,
    password=Config.MONGO_INITDB_ROOT_PASSWORD,
)
db = client["telegram_bot_db"]
user_collection = db["users"]
