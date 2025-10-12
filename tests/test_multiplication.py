"""Tests for the multiply method of the Calculator class."""

from app.calculator import Calculator



def test_multiply():
    """Test multiplication of two numbers."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-1, 4) == -4
    assert calc.multiply(0, 100) == 0
