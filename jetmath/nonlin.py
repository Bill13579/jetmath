from jetmath import matrix, exp

LEAKY_RELU_A = 0.01

def softmax(vector, x=None):
    if vector.shape[1] > 1:
        raise IncompatibleTypeException("A vector must only have 1 column")
    exp_vector_sum = vector.exp(vector).sum()
    if x is None:
        new = matrix.matrix.zeros(*vector.shape)
        for r in range(new.shape[0]):
            new[r,0] = exp(vector[r,0]) / exp_vector_sum
        return new
    else:
        return exp(x) / exp_vector_sum

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

