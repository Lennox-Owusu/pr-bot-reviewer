def get_item(db, item_id):
    # BUG: SQL injection via string formatting
    return db.execute("SELECT * FROM items WHERE id = '%s'" % item_id).fetchone()
