import bcrypt
import sqlite3
from db import DB_NAME

# -------------------------------
# REGISTER USER
# -------------------------------
def register_user(email, password):
    """
    Registers a new user
    Returns: (success: bool, message: str)
    """
    if get_user(email):
        return False, "Email already registered"

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed))
    conn.commit()
    conn.close()
    return True, "Registration successful"

# -------------------------------
# LOGIN USER
# -------------------------------
def login_user(email, password):
    """
    Logs in a user
    Returns: (success: bool, message: str, user: tuple)
    """
    user = get_user(email)
    if not user:
        return False, "Email not registered", None
    stored_hash = user[2]  # user = (id, email, password)
    if bcrypt.checkpw(password.encode(), stored_hash):
        return True, "Login successful", user
    else:
        return False, "Incorrect password", None

# -------------------------------
# GET USER
# -------------------------------
def get_user(email):
    """
    Fetches user from DB by email
    Returns: user tuple (id, email, password) or None
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    return user
