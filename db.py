import sqlite3

DB_NAME = "vault.db"

# -------------------------------
# CREATE TABLES
# -------------------------------
def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    # Vault table with category and favorite
    c.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            site TEXT,
            username TEXT,
            password TEXT,
            category TEXT,
            favorite INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    # Password history table
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            site TEXT,
            username TEXT,
            password TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# -------------------------------
# ADD PASSWORD
# -------------------------------
def add_password(user_id, site, username, password, category="", favorite=0):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO vault (user_id, site, username, password, category, favorite)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, site, username, password, category, favorite))
    conn.commit()
    conn.close()

# -------------------------------
# GET PASSWORDS
# -------------------------------
def get_passwords(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM vault WHERE user_id = ?", (user_id,))
    data = c.fetchall()
    conn.close()
    return data

# -------------------------------
# DELETE PASSWORD
# -------------------------------
def delete_password(password_id, user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM vault WHERE id = ? AND user_id = ?", (password_id, user_id))
    conn.commit()
    conn.close()

# -------------------------------
# GET DASHBOARD STATS
# -------------------------------
def get_stats(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM vault WHERE user_id = ?", (user_id,))
    total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM vault WHERE user_id = ? AND LENGTH(password) < 8", (user_id,))
    weak = c.fetchone()[0]
    conn.close()
    return total, weak

# -------------------------------
# ADD TO HISTORY
# -------------------------------
def add_to_history(user_id, site, username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO history (user_id, site, username, password)
        VALUES (?, ?, ?, ?)
    """, (user_id, site, username, password))
    conn.commit()
    conn.close()

# -------------------------------
# TOGGLE FAVORITE
# -------------------------------
def toggle_favorite(password_id, user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT favorite FROM vault WHERE id = ? AND user_id = ?", (password_id, user_id))
    current = c.fetchone()
    if current:
        new_val = 0 if current[0] == 1 else 1
        c.execute("UPDATE vault SET favorite = ? WHERE id = ? AND user_id = ?", (new_val, password_id, user_id))
        conn.commit()
    conn.close()
