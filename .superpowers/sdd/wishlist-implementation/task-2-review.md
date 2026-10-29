diff --git a/backend/.env b/backend/.env
new file mode 100644
index 0000000..590ffbb
--- /dev/null
+++ b/backend/.env
@@ -0,0 +1,4 @@
+SMTP_SERVER=smtp.gmail.com
+SMTP_PORT=587
+SMTP_USER=your_email@gmail.com
+SMTP_PASSWORD=your_app_password
diff --git a/backend/email_service.py b/backend/email_service.py
new file mode 100644
index 0000000..4dde765
--- /dev/null
+++ b/backend/email_service.py
@@ -0,0 +1,29 @@
+import smtplib
+from email.mime.text import MIMEText
+from email.mime.multipart import MIMEMultipart
+import os
+from dotenv import load_dotenv
+from schemas import WishlistRequest
+
+load_dotenv()
+
+def send_wishlist_email(data: WishlistRequest):
+    msg = MIMEMultipart()
+    msg['From'] = os.getenv('SMTP_USER')
+    msg['To'] = 'parveshkumara001@gmail.com'
+    msg['Subject'] = f"New Wishlist from {data.name}"
+    
+    body = f"""
+    <h2>New Wishlist Submission</h2>
+    <p><b>Name:</b> {data.name}</p>
+    <p><b>Items:</b> {data.item_names}</p>
+    <p><b>Priority:</b> {data.priority}</p>
+    <p><b>Link:</b> <a href='{data.item_link}'>{data.item_link}</a></p>
+    """
+    msg.attach(MIMEText(body, 'html'))
+    
+    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
+        server.starttls()
+        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
+        server.send_message(msg)
+    return True
