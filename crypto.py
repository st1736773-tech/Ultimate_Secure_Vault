from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# -------------------------------
# GENERATE / LOAD KEY
# -------------------------------
def generate_key():
    """
    Generate a key if not exists and save to file
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

# -------------------------------
# LOAD KEY
# -------------------------------
def load_key():
    """
    Load the Fernet key from file
    """
    with open(KEY_FILE, "rb") as f:
        key = f.read()
    return key

# -------------------------------
# ENCRYPT PASSWORD
# -------------------------------
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# -------------------------------
# DECRYPT PASSWORD
# -------------------------------
def decrypt_password(enc_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(enc_password.encode()).decode()
