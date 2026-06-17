"""Scenario 6 — clean dedup test (Ticket 16).
Step 1: open a PR with this file. The bot should flag the divide() zero-check bug.
Step 2: append the add() function shown in the playbook (AFTER divide) and push.
        divide() is untouched and its line number does not move.
Expected on re-review: the divide() comment is NOT posted again."""


def divide(a, b):
    # divides two numbers, no zero check
    return a / b
