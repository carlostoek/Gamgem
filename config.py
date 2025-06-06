import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID")) # Asegúrate de que sea un int
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///gamification.db") # Default para desarrollo
    CHANNEL_ID = int(os.getenv("CHANNEL_ID")) # ID del canal de Telegram
