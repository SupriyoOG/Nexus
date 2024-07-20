import json
import hashlib
import os
from colorama import Fore

def get_stored_password(file_path='password.json'):
    """Retrieve the stored password hash from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get('password_hash')

def verify_password(input_password):
    """Verify if the provided password is not empty and matches the stored hash."""
    if not input_password.strip():
        print(Fore.RED + "Password cannot be empty. Try again.")
        return False
    
    stored_password_hash = get_stored_password()
    return hashlib.sha256(input_password.encode()).hexdigest() == stored_password_hash

def store_password(password, file_path='password.json'):
    """Hash and store the password in a JSON file."""
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with open(file_path, 'w') as file:
        json.dump({'password_hash': password_hash}, file)

def change_password():
    """Change the password and store the new hash."""
    while True:
        old_password = input("Enter old password: ")
        if old_password.strip():
            password_hash = get_stored_password()
            if hashlib.sha256(old_password.encode()).hexdigest() == password_hash:
                break
        else:
            print(Fore.RED + "Old password cannot be empty. Try again.")
    
    if not verify_password(old_password):
        print(Fore.RED + "Incorrect password. Try again.")
        return
    
    while True:
        new_password = input("Enter new password: ")
        if new_password.strip():  # Check if new password is not empty or only whitespace
            break
        else:
            print(Fore.RED + "New password cannot be empty. Try again.")
    
    while True:
        confirm_password = input("Confirm new password: ")
        if confirm_password.strip():  # Check if confirm password is not empty or only whitespace
            break
        else:
            print(Fore.RED + "Confirmation password cannot be empty. Try again.")
    
    if new_password == confirm_password:
        store_password(new_password)
        print(Fore.GREEN + "Password changed successfully.")
    else:
        print(Fore.RED + "Passwords do not match. Try again.")
