import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def generate_otp(length=6):
    return "".join([str(random.randint(0,9)) for _ in range(length)])

def send_otp(to_email, otp):
    try:
        GMAIL_USER = st.secrets.get("GMAIL_USER")
        GMAIL_PASSWORD = st.secrets.get("GMAIL_PASSWORD")
        if not GMAIL_USER or not GMAIL_PASSWORD:
            return False
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = to_email
        msg["Subject"] = "Your OTP for Ultimate Secure Vault"
        body = f"Your OTP is: {otp}"
        msg.attach(MIMEText(body,"plain"))
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(GMAIL_USER,GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Failed to send OTP:", e)
        return False
