import pytest
from app.calculator import divide

def test_division():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(5.0, 2.5) == 2.0

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
