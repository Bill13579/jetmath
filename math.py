def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

from jetm import matrix

def zeros(rows, cols):
    return matrix([[0.0] * cols] * rows)
