"""Tests for the divide method of the Calculator class."""

import pytest

from app.calculator import Calculator




def test_divide():
    """Test division of two numbers."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2


def test_divide_by_zero():
    """Test division by zero raises an error."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
