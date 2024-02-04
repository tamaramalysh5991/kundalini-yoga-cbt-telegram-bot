import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Telegram Bot Token
    TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")

    # MongoDB Configuration
    MONGODB_URI = os.getenv("MONGODB_URI")
    MONGODB_NAME = os.getenv("MONGODB_NAME")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Default to 'INFO' if not specified
