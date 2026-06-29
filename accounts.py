import sqlite3


def find_account(db, name):
    query = "SELECT * FROM accounts WHERE name = '" + name + "'"
    cur = db.execute(query)
    return cur.fetchall()
