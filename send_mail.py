import smtplib
import os
import datetime
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

today = datetime.date.today()

msg = EmailMessage()
msg["Subject"] = f"Your feed for {today.strftime('%d %b %Y')}"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "benjacoblee@gmail.com"
# msg.set_content("How about dinner at 6pm this Saturday?")

html = open("feed.html")
html = str(html.read())

msg.add_alternative(html, subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
