import pytest

from calculator_clean import divide


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (-10, 2, -5.0),
    (10, -2, -5.0),
    (0, 5, 0.0),
    (7, 2, 3.5),
])
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="must not be zero"):
        divide(1, 0)
