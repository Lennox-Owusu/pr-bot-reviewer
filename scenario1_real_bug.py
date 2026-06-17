"""Scenario 1 — happy-path review. Contains one clear, real bug the AI should
flag on a changed line, plus benign code. Verifies the bot produces a valid
finding anchored to the correct line (WOULD_POST in the dry-run audit)."""


def get_user_by_id(db, user_id):
    # BUG (intentional): raw string formatting -> SQL injection.
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    return db.execute(query).fetchone()


def average(numbers):
    # BUG (intentional): no guard for empty list -> ZeroDivisionError.
    return sum(numbers) / len(numbers)


def greet(name):
    return f"Hello, {name}!"
