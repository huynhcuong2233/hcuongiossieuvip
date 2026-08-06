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



# ==========================
# NẠP TIỀN MOMO
# ==========================

def create_deposit(user_id, amount, content):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO deposits(
        user_id,
        amount,
        content
    )
    VALUES(?,?,?)
    """, (
        user_id,
        amount,
        content
    ))

    conn.commit()
    conn.close()



def deposit_exists(content):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM deposits WHERE content=?",
        (content,)
    )

    row = cur.fetchone()

    conn.close()

    return row is not None



def confirm_deposit(content):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT user_id, amount
    FROM deposits
    WHERE content=?
    AND status='pending'
    """, (content,))

    row = cur.fetchone()

    if row:

        user_id, amount = row

        cur.execute("""
        UPDATE users
        SET balance = balance + ?,
            total_deposit = total_deposit + ?
        WHERE user_id=?
        """,
        (
            amount,
            amount,
            user_id
        ))

        cur.execute("""
        UPDATE deposits
        SET status='done'
        WHERE content=?
        """,
        (content,))


    conn.commit()
    conn.close()

    return row
