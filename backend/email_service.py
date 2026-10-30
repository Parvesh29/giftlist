import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from .schemas import WishlistRequest

load_dotenv()

def send_wishlist_email(data: WishlistRequest):
    # Fallback to default Gmail settings if .env is missing
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = os.getenv('SMTP_PORT', '587')
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASSWORD')

    if not smtp_user or not smtp_pass:
        raise Exception("SMTP_USER or SMTP_PASSWORD not found in environment variables")

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = 'parveshkumara001@gmail.com'
    msg['Subject'] = f"New Wishlist from {data.name}"
    
    body = f"""
    <h2>New Wishlist Submission</h2>
    <p><b>Name:</b> {data.name}</p>
    <p><b>Items:</b> {data.item_names}</p>
    <p><b>Priority:</b> {data.priority}</p>
    <p><b>Link:</b> <a href='{data.item_link}'>{data.item_link}</a></p>
    """
    msg.attach(MIMEText(body, 'html'))
    
    with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    return True
