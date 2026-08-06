import sqlite3
import os

DB_NAME = "data/database.db"


def connect():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        balance INTEGER DEFAULT 0,
        total_deposit INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS deposits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        content TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, full_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users(user_id, username, full_name)
    VALUES (?, ?, ?)
    """, (user_id, username, full_name))

    conn.commit()
    conn.close()


def get_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    user = cur.fetchone()

    conn.close()
    return user


def get_balance(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cur.fetchone()

    conn.close()

    return row[0] if row else 0


def add_balance(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET balance = balance + ?,
        total_deposit = total_deposit + ?
    WHERE user_id=?
    """, (amount, amount, user_id))

    conn.commit()
    conn.close()


def minus_balance(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET balance = balance - ?
    WHERE user_id=?
    """, (amount, user_id))

    conn.commit()
    conn.close()


def add_deposit(user_id, amount, content, status="pending"):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO deposits(user_id, amount, content, status)
    VALUES (?, ?, ?, ?)
    """, (user_id, amount, content, status))

    conn.commit()
    conn.close()
