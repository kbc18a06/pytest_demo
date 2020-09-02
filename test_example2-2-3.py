from calc import Calculator
import pytest
@pytest.fixture(scope="module")
def calc():
    c = Calculator()
    print("create calculator")
    return c
def test_add(calc):
    assert calc.add(5, 2) == 7
def test_sub(calc):
    assert calc.sub(5, 2) == 3
def test_mul(calc):
    assert calc.mul(5, 2) == 10
def test_div(calc):
    assert calc.div(5, 2) == 2
def test_square(calc):
    assert calc.square(5) == 25
def test_cube(calc):
    assert calc.cube(5) == 125