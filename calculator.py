"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise Zero_Division_Error("Can't divide by Zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm undefined for these values: base must be > 0 and ≠ 1; argument must be > 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b


