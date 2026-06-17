from googleapiclient.discovery import build
import imaplib
import email
from config import ( EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    GMAIL,
    IMAP_PORT)
def get_unread_emails():
    # service = build("gmail", "v1",credentials=creds)

    # result = service.user().message().list(
    #     userid = "me",
    #     q="is:unread"
    # ).execute()
    mail = imaplib.IMAP4_SSL(GMAIL, 993)

    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    mail.select("INBOX")
    emails = []
    status, messages = mail.search(None, "ALL")

    for num in messages[0].split():
    
        _, data = mail.fetch(num, "(RFC822)")

        msg = email.message_from_bytes(data[0][1])

        emails.append({
            "From": msg.get("From"),
            "subject": msg.get("Subject")
        })

    mail.logout()
    
    return emails
