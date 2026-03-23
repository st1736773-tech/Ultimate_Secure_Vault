# Ultimate_Secure_Vault-Enterprise-Password-Manager-.
# Ultimate Secure Vault 🔒

**Ultimate Secure Vault** is a production-level, enterprise-ready **Password Manager** built with **Python & Streamlit**.  
It provides **secure, encrypted password storage**, multi-user authentication, and a **modern website-like interface**.

---

## 🌟 Features

### Core Features
- Multi-user authentication (Register + Login)
- Each user has their own encrypted password vault
- Password hashing using **bcrypt**
- Password encryption using **Fernet (cryptography)**
- SQLite database with proper schema
- Real Email OTP verification (Gmail SMTP, optional)
- Session management with auto logout
- Import / Export CSV functionality
- Password strength checker
- AI strong password generator

### Premium UI & UX
- Modern, website-like multi-page design
- Sidebar navigation for easy access
- Dashboard with stats: total passwords, weak passwords
- Vault cards with **favorite/star**, show/hide, and copy password
- Fun animations (`st.balloons()`) when adding passwords
- Clean white/light theme (can switch to dark if preferred)

### Security
- No plain text passwords stored
- Encrypted vault storage
- Hashed user passwords
- Optional OTP verification
- Secure session management

---

## 📂 Repo Structure

```text
ultimate_secure_vault/
│
├── app.py           # Main Streamlit app
├── db.py            # Database: users, passwords, history
├── auth.py          # Authentication: register/login
├── utils.py         # Password strength, generator, CSV import/export
├── crypto.py        # Encryption/decryption (Fernet)
├── email_otp.py     # Email OTP functions (Gmail SMTP)
├── requirements.txt # Python dependencies
├── secret.key       # Fernet key (auto-generated)
└── README.md        # Project description
