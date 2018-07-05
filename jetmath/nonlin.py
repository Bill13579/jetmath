from math import exp

LEAKY_RELU_A = 0.01

def softmax(x, vector):
    if vector.shape[1] > 1:
        raise IncompatibleTypeException("A vector must only have 1 column")
    return exp(x) / vector.exp(vector).sum()

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

class IncompatibleTypeException(Exception):
    pass

