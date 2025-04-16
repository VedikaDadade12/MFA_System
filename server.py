from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

otp_store = {}  # Store OTPs per email

# Email configuration
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "vedikadabade8@gmail.com"  # 🔹 Replace with your Gmail
EMAIL_PASSWORD = "cjrt iuwk sxjy uohh"  # 🔹 Replace with your Gmail App Password

# Function to send email
def send_otp_email(email, otp):
    subject = "Your OTP Code for Verification"
    message = f"Hello,\n\nYour OTP code is: {otp}\n\nPlease enter this code to verify your email.\n\nThank you!"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, email, msg.as_string())
        server.quit()
        print(f"✅ OTP sent to {email}")
        return True
    except Exception as e:
        print(f"❌ Error sending OTP: {e}")
        return False

# Route to generate OTP & send email
@app.route("/generate_email_otp", methods=["POST"])
def generate_email_otp():
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    otp = str(random.randint(1000, 9999))
    otp_store[email] = otp  # Store OTP for this email

    if send_otp_email(email, otp):
        return jsonify({"message": "OTP sent successfully!"})
    return jsonify({"error": "Failed to send OTP"}), 500

# Route to verify OTP
@app.route("/verify_email_otp", methods=["POST"])
def verify_email_otp():
    data = request.json
    email = data.get("email")
    entered_otp = data.get("otp")

    if not email or not entered_otp:
        return jsonify({"error": "Email and OTP are required"}), 400

    stored_otp = otp_store.get(email)
    if stored_otp and entered_otp == stored_otp:
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Invalid OTP"}), 400

if __name__ == "__main__":
    app.run(debug=True)
