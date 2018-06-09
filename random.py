import random
from jetm import matrix

def seed(seed):
    random.seed(random.SystemRandom().randint(0, 2147483647))

def rand(rows, cols):
    m = matrix.zeros(rows, cols)
    for r in range(m.shape[0]):
        for c in range(m.shape[1]):
            m[r,c] = random.random()
    return m

