import smtplib
import random
import re
import dns.resolver  # You may need to install dnspython package for DNS lookups
from functions.password import store_password
from colorama import Fore

# Function to validate email format
def is_valid_email_format(email):
    # Regular expression for basic email format validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

# Function to check if domain has valid MX records
def has_valid_mx_records(email):
    domain = email.split('@')[1]
    try:
        # Perform DNS MX record lookup
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

# Function to send verification email
def send_verification_email(receiver_email, verification_code):
    sender_email = "namanchoubey69@gmail.com"  # Your Gmail address
    app_password = "byds azfr lvos bkae"  # App password generated from Google Account settings

    subject = "Password Reset Verification Code"
    body = f"Your verification code is: {verification_code}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message)
        print("Verification code sent successfully.")
        return True
    except Exception as e:
        print(f"Failed to send verification code: {e}")
        return False

def generate_verification_code():
    return str(random.randint(100000, 999999))

def change_password1():
    """Change the password and store the new hash."""
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    if new_password == confirm_password:
        store_password(new_password)
        print(Fore.GREEN + "Password changed successfully.")
    else:
        print(Fore.RED + "Passwords do not match. Try again.")


def main():
    receiver_email = input("Enter your email address: ")

    if not is_valid_email_format(receiver_email):
        print("Invalid email format. Please enter a valid email address.")
        return
    
    if not has_valid_mx_records(receiver_email):
        print("Invalid email domain. Please enter a valid email address.")
        return

    verification_code = generate_verification_code()
    if send_verification_email(receiver_email, verification_code):
        print("Verification code sent. Please check your email.")
        entered_code = input("Enter the verification code received: ")

        if entered_code == verification_code:
            print("Verification successful. Proceed to reset your password.")
            change_password1()
        else:
            print("Verification code does not match. Please try again.")
    else:
        print("Failed to send verification code. Please try again later.")

