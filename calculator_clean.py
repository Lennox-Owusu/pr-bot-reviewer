"""Safe arithmetic helpers."""


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Divisor must not be zero.")
    return a / b
