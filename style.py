"""BUG-3 retest — this file has NO real bugs, only cosmetic/style nitpicks.
If the bot posts these as INLINE comments (severity warning+), BUG-3 reproduces.
If it routes them to the summary instead, BUG-3 does not reproduce."""
import os
import sys


def calculate_total(items):
    total=0
    for i in items:
        total=total+i
    return total
