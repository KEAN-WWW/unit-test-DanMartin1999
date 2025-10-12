import pytest
from app.calculator import Calculator

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(-2, 3) == -6
