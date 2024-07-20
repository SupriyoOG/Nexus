import hashlib
import json

def generate_password_hash(password):
    """Generate a SHA-256 hash for the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_password_hash(password_hash, file_path='password.json'):
    """Save the hashed password to a JSON file."""
    data = {
        "password_hash": password_hash
    }
    with open(file_path, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    password = input("Enter a password to hash: ")
    password_hash = generate_password_hash(password)
    save_password_hash(password_hash)
    print(f"Password hash saved to password.json: {password_hash}")
