import base64
from email.mime.text import MIMEText

from app.tools.gmail_service import get_gmail_service
from app.tools.contacts import get_email


def send_email(parameters):

    service = get_gmail_service()

    name = parameters.get("recipient")
    recipient = get_email(name)

    if recipient is None:
        print("❌ Contact not found.")
        return

    subject = parameters.get("subject", "No Subject")
    body = parameters.get("body", "")

    message = MIMEText(body)

    message["to"] = recipient
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()

    print(f"\n✅ Email sent successfully to {recipient}")