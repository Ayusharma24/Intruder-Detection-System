import os
import smtplib
import numpy as np
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart

def send_alert(email_subject, email_body, to_email, image_path=None):
    """
    Sends an email alert with an optional attachment.
    Uses SMTP credentials from environment variables.
    """
    EMAIL_ADDRESS = os.getenv("SMTP_EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("SMTP_EMAIL_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

    msg = MIMEMultipart()
    msg["Subject"] = email_subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.attach(MIMEText(email_body, "plain"))

    if image_path:
        with open(image_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(image_path)}")
            msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print("✅ Alert sent successfully!")
    except smtplib.SMTPException as e:
        print(f"⚠️ Error sending email: {e}")

def verify_email(to_email):
    """
    Sends a verification code to the recipient's email.
    Returns the generated verification code.
    """
    verification_code = str(np.random.randint(100000, 999999))
    send_alert("Email Verification", f"Your verification code is {verification_code}", to_email)
    return verification_code
