from __future__ import absolute_import
from math import floor

E = 2.71828182845904523536028747135266250
PI = 3.14159265358979323846264338327950288
PHI = 1.61803398874989484820458683436563812

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return float(x) / float(y)

def exp(x):
    return E ** x

def identity(x):
    return x

def sepd(x):
    return floor(x), x % 1

