"""Tests for the add method of the Calculator class."""

from app.calculator import Calculator



def test_add():
    """Test addition of two numbers."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
