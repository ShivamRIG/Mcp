import requests
from config import (
    Telegram_bot_token,
    Telegram_chat_session
)
BOT_token= ""
chat_session = ""

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text,
        },
        timeout=10,
    )