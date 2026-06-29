import sqlite3


def find_account(db, name):
    query = "SELECT * FROM accounts WHERE name = ?"
    cur = db.execute(query, (name,))
    return cur.fetchall()
