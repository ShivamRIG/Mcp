from googleapiclient.discovery import build
import imaplib
import email
from config import ( EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    IMAP_SERVER,
    IMAP_PORT)
def get_unread_emails():
    service = build("gmail", "v1",credentials=creds)

    result = service.user().message().list(
        userid = "me",
        q="is:unread"
    ).execute()
    EMAIL = "yourname@rhrk.uni-kl.de"
    PASSWORD = "your_password"

    mail = imaplib.IMAP4_SSL("mail.uni-kl.de", 993)

    mail.login(EMAIL, PASSWORD)

    mail.select("INBOX")

    status, messages = mail.search(None, "UNSEEN")

    for num in messages[0].split():
        _, data = mail.fetch(num, "(RFC822)")
    
        msg = email.message_from_bytes(data[0][1])
    
        print("Subject:", msg["Subject"])
        print("From:", msg["From"])
    
    return result.get("messages",[])
