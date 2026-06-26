# test_percent.py
import pytest
from percent import percentage

def test_percentage_normal():
    assert percentage(50, 200) == 25.0

def test_percentage_full():
    assert percentage(100, 100) == 100.0

def test_percentage_zero_part():
    assert percentage(0, 100) == 0.0

def test_percentage_zero_whole_raises():
    with pytest.raises(ValueError, match="must not be zero"):
        percentage(50, 0)

def test_percentage_float_inputs():
    assert percentage(1.5, 3.0) == pytest.approx(50.0)

def test_percentage_negative_part():
    assert percentage(-50, 200) == -25.0
def percentage(part, whole):
    """
    Calculate the percentage of part relative to whole.

    Args:
        part (float): The partial value.
        whole (float): The total value. Must not be zero.

    Returns:
        float: The percentage value (0-100 scale).

    Raises:
        ValueError: If whole is zero.
    """
    if whole == 0:
        raise ValueError("'whole' must not be zero to avoid division by zero.")
    return part / whole * 100
