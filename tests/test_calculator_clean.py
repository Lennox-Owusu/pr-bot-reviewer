import pytest

from calculator_clean import divide


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="must not be zero"):
        divide(1, 0)
