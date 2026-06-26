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
        for column, value in filters:
            if column not in allowed_columns:
            if column not in allowed_columns:
                raise ValueError(f"Disallowed filter column: {column}")
            query += f" AND {column} = ?"
            params.append(value)
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return rows
    # Remove all lines 20–37 entirely. The complete, correct function is:
    
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
    query = "SELECT * FROM users WHERE role = ?"
    params = [role]
    for f in filters:
        # Each filter must be a validated column/value pair, never raw user input
    allowed_columns = {"status", "department", "active"}  # tailor to your schema
    for column, value in filters:
        if column not in allowed_columns:
            raise ValueError(f"Disallowed filter column: {column}")
        query += f" AND {column} = ?"
        params.append(value)
    cursor.execute(query, params)
 # Delete lines 27–28 entirely as part of removing the entire dead code block (lines 20–37).
    # Filters must be expressed as (column, value) tuples; never accept raw SQL fragments from callers.
    for column, value in filters:
        allowed_columns = {"status", "department", "active"}  # define per your schema
        if column not in allowed_columns:
            raise ValueError(f"Disallowed filter column: {column}")
        query += f" AND {column} = ?"
        params.append(value)
    cursor.execute(query, params)
 # Delete line 36. The correct parameterized call is already present at line 35:
 # cursor.execute(query, params)
    rows = cursor.fetchall()
# Add a test file, e.g. test_userquery.py, covering:
# 1. Normal retrieval with default role
# 2. Custom role value
# 3. Valid filters list
# 4. Disallowed column name raises ValueError
# 5. Empty result set
# Create test_userquery.py with content such as:

import pytest
from unittest.mock import patch, MagicMock
from userquery import load_users

def test_load_users_default_role():
    with patch("userquery.sqlite3.connect") as mock_conn:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "alice", "user")]
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        result = load_users(":memory:")
        assert result == [(1, "alice", "user")]
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM users WHERE role = ?", ["user"]
        )

def test_load_users_custom_role():
    with patch("userquery.sqlite3.connect") as mock_conn:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        result = load_users(":memory:", role="admin")
        assert result == []

def test_load_users_valid_filter():
    with patch("userquery.sqlite3.connect") as mock_conn:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(2, "bob", "user")]
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        result = load_users(":memory:", filters=[("status", "active")])
        assert result == [(2, "bob", "user")]
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM users WHERE role = ? AND status = ?", ["user", "active"]
        )

def test_load_users_disallowed_column_raises():
    with patch("userquery.sqlite3.connect"):
        with pytest.raises(ValueError, match="Disallowed filter column: evil"):
            load_users(":memory:", filters=[("evil", "1 OR 1=1")])

def test_load_users_empty_result():
    with patch("userquery.sqlite3.connect") as mock_conn:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        result = load_users(":memory:")
        assert result == []

def test_load_users_db_connection_failure():
    with patch("userquery.sqlite3.connect", side_effect=Exception("DB error")):
        with pytest.raises(Exception, match="DB error"):
            load_users(":memory:")
