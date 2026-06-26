import sqlite3


def load_users(db_path, role="user", filters=None):
    if filters is None:
        filters = []
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE role = ?"
        params = [role]
        for column, value in filters:
            allowed_columns = {"status", "department", "active"}
            if column not in allowed_columns:
                raise ValueError(f"Disallowed filter column: {column}")
            query += f" AND {column} = ?"
            params.append(value)
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return rows
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE role = ?"
    params = [role]
    for f in filters:
        # Each filter must be a validated column/value pair, never raw user input
        query += " AND " + f
    cursor.execute(query, params)
    for f in filters:
    # Filters must be expressed as (column, value) tuples; never accept raw SQL fragments from callers.
    for column, value in filters:
        allowed_columns = {"status", "department", "active"}  # define per your schema
        if column not in allowed_columns:
            raise ValueError(f"Disallowed filter column: {column}")
        query += f" AND {column} = ?"
        params.append(value)
    cursor.execute(query, params)
    cursor.execute(query)
    rows = cursor.fetchall()
# Add a test file, e.g. test_userquery.py, covering:
# 1. Normal retrieval with default role
# 2. Custom role value
# 3. Valid filters list
# 4. Disallowed column name raises ValueError
# 5. Empty result set
# 6. Database connection failure (mock sqlite3.connect to raise)
