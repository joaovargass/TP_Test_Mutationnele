"""
======= TESTS =======
"""
from calculator import *

def test_sum():
    assert sum(2,3) == 5

def test_sub():
    assert sub(5,3) == 2

def test_mult():
    assert mult(3,4) == 12
    assert mult(2.5, 4) == 10

def test_div():
    assert div(17,2) == 8.5
    assert div(20,4) == 5
    assert div(20,0) == "Division by zero"
    assert div(21,4) == 5.25

def test_sqRoot():
    assert sqRoot(16) == 4
    assert sqRoot(2) == 1.41421
    assert sqRoot(-1) == "Negative number"
    assert sqRoot(0) == 0

def test_power():
    assert power(2,3) == 8
    assert power(4,0.5) == 2

def test_intToBin():
    assert intToBin(10) == 1010
    assert intToBin(255) == 11111111
    assert intToBin(19) == 10011

if __name__ == '__main__':
    test_power()
    test_div()
    test_mult()
    test_intToBin()
    test_sqRoot()
    test_sub()
    test_sum()