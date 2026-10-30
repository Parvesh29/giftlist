import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from .schemas import WishlistRequest

load_dotenv()

def send_wishlist_email(data: WishlistRequest):
    # Use the API key from environment variables
    api_key = os.getenv('SENDGRID_API_KEY')
    
    if not api_key:
        raise Exception("SENDGRID_API_KEY not found in environment variables")

    sg = SendGridAPIClient(api_key)
    
    # The 'from_email' must be a verified sender in your SendGrid account
    from_email = os.getenv('SENDGRID_FROM_EMAIL', 'parveshkumara001@gmail.com')
    to_email = 'parveshkumara001@gmail.com'
    
    html_content = f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
        <h2 style="color: #4a90e2; text-align: center;">🎁 New Wishlist Submission!</h2>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
        <p><strong>Name:</strong> {data.name}</p>
        <p><strong>Items:</strong> {data.item_names}</p>
        <p><strong>Priority:</strong> {data.priority}</p>
        <p><strong>Link:</strong> <a href="{data.item_link}">{data.item_link}</a></p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
        <p style="font-size: 12px; color: #888; text-align: center;">Sent via Wishlist App</p>
    </div>
    """
    
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=f"New Wishlist from {data.name}",
        html_content=html_content
    )
    
    response = sg.send(message)
    
    # SendGrid returns 202 Accepted if successful
    if response.status_code >= 200 and response.status_code < 300:
        return True
    else:
        raise Exception(f"SendGrid error: {response.status_code}")
