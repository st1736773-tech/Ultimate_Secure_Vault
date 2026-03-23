from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


# -------------------------------
# GENERATE & SAVE KEY
# -------------------------------
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)


# -------------------------------
# LOAD KEY
# -------------------------------
def load_key():
    return open(KEY_FILE, "rb").read()


# -------------------------------
# ENCRYPT PASSWORD
# -------------------------------
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode()


# -------------------------------
# DECRYPT PASSWORD
# -------------------------------
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()
