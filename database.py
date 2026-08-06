import sqlite3
from config import DATABASE_NAME


def connect():
    return sqlite3.connect(DATABASE_NAME)


def setup_database():
    conn = connect()
    cur = conn.cursor()

    # Người dùng
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        fullname TEXT,
        balance INTEGER DEFAULT 0,
        total_deposit INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Giao dịch nạp tiền
    cur.execute("""
    CREATE TABLE IF NOT EXISTS deposits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        content TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Đơn hàng
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price INTEGER,
        api_key TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, fullname):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users(user_id, username, fullname)
    VALUES(?,?,?)
    """, (user_id, username, fullname))

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

    if row:
        return row[0]

    return 0


def add_balance(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET
        balance = balance + ?,
        total_deposit = total_deposit + ?
    WHERE user_id=?
    """, (amount, amount, user_id))

    conn.commit()
    conn.close()


def remove_balance(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET balance = balance - ?
    WHERE user_id=?
    """, (amount, user_id))

    conn.commit()
    conn.close()


def create_order(user_id, product, price, api_key):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO orders(
        user_id,
        product,
        price,
        api_key
    )
    VALUES(?,?,?,?)
    """, (user_id, product, price, api_key))

    conn.commit()
    conn.close()


def get_orders(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT product, price, created_at
    FROM orders
    WHERE user_id=?
    ORDER BY id DESC
    """, (user_id,))

    rows = cur.fetchall()

    conn.close()

    return rows
