from jetm import matrix

E = 2.71828182845904523536028747135266250

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exp(x):
    return E ** x

LEAKY_RELU_A = 0.01

def identity(x):
    return x

def sigmoid(x):
    return 1/(1 + exp(-x))

def relu(x):
    return max(0,x)

def leaky_relu(x):
    return x if x > 0 else LEAKY_RELU_A*x

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

def relu_p(x):
    return 1 if x > 0 else 0

def leaky_relu_p(x):
    return 1 if x > 0 else LEAKY_RELU_A

def zeros(rows, cols):
    return matrix([[0.0] * cols] * rows)
