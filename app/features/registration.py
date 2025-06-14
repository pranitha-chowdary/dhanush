# app/features/registration.py

import re
import hashlib

# Mock database
users_db = {}

def is_valid_email(email):
    """Simple regex-based email validator."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    """Main logic to register a user."""
    if not username or not email or not password:
        return {"status": "error", "message": "All fields are required."}

    if not is_valid_email(email):
        return {"status": "error", "message": "Invalid email format."}

    if email in users_db:
        return {"status": "error", "message": "Email already registered."}

    # Store the user with hashed password
    users_db[email] = {
        "username": username,
        "email": email,
        "password": hash_password(password)
    }

    return {"status": "success", "message": "User registered successfully."}
