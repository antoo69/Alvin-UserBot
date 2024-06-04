from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv("config.env")

API_KEY = os.environ.get("API_KEY", 22839539)
API_HASH = os.environ.get("API_HASH", 9ae7b55a690c6dbb2ea2110d887e91c7)

bot = TelegramClient('userbot', API_KEY, API_HASH)
bot.start()
