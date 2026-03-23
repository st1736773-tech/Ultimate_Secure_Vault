import random
import string
import csv
from io import StringIO


# -------------------------------
# PASSWORD STRENGTH CHECKER
# -------------------------------
def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


# -------------------------------
# STRONG PASSWORD GENERATOR
# -------------------------------
def generate_strong_password(length=16):
    if length < 12:
        length = 12  # minimum for strong passwords

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# -------------------------------
# EXPORT PASSWORDS TO CSV
# -------------------------------
def export_to_csv(passwords):
    """
    passwords: list of tuples (site, username, password)
    returns CSV string
    """
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Site", "Username", "Password"])
    for entry in passwords:
        writer.writerow([entry[1], entry[2], entry[3]])  # site, username, password
    return output.getvalue()


# -------------------------------
# IMPORT PASSWORDS FROM CSV
# -------------------------------
def import_from_csv(csv_file):
    """
    csv_file: Uploaded file object from Streamlit
    returns list of tuples (site, username, password)
    """
    decoded = csv_file.read().decode("utf-8")
    reader = csv.DictReader(StringIO(decoded))
    entries = []
    for row in reader:
        entries.append((row["Site"], row["Username"], row["Password"]))
    return entries
