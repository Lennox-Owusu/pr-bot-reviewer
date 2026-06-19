def get_user(db, user_id):
    # BUG: SQL injection via string formatting
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    return db.execute(query).fetchone()

# re-trigger review
