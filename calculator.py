"""
Aplication - Calculator
Authors - Nicolau Pereira Alff and João Vitor Vargas Soares
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
    if y == 0:
        return "Division by zero"
    elif x%y == 0:
        return x/y
    else:
        return float(x/y)

def sqRoot(x):
    if x < 0:
        return "Negative number"
    result = math.sqrt(x)
    return round(result, 5)

def power(x,y):
    return x**y

def intToBin(x):
    newStr = bin(x)
    newStr = newStr[2:]
    newNr = int(newStr)
    return newNr
