"""
Aplication - Calculator
Author - Nicolau Pereira Alff
Objective - Implement a calculator which will calculate: addition, subtraction, 
                                                         multiplication, division, 
                                                         square root, potentiation

            It will also convert integers to binary numbers

"""
import math


def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    if x%y == 0:
        return x/y
    else:
        return float(x)/y

def sqRoot(x):
    result = math.sqrt(x)
    if (type(result) == int):
        return result
    else:
        return round(result, 5)

def power(x,y):
    return x**y

def intToBin(x):
    newStr = bin(x)
    newStr = newStr[2:]
    newNr = int(newStr)
    return newNr



"""
======= TESTS =======
"""


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

def test_sqRoot():
    assert sqRoot(16) == 4
    assert sqRoot(2) == 1.41421

def test_power():
    assert power(2,3) == 8
    assert power(4,0.5) == 2

def test_intToBin():
    assert intToBin(10) == 1010
    assert intToBin(255) == 11111111
    assert intToBin(19) == 10011

