from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("Email_Address")
EMAIL_PASSWORD = os.getenv("Email_password")

IMAP_SERVER= os.getenv("IMAP_Server","mail.uni.kl.de")
IMAP_PORT= int (os.getenv("IMAP_port",993))

# telegram

Telegram_bot_token = os.getenv("Telegram_bot_token ")

Telegram_chat_session = os.getenv("Session")