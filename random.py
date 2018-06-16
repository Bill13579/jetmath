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

def randd():
    return random.random()

def randruns(p, s, f, params=(), iterations=1):
    results = []
    for i in range(iterations):
        results.append(randrun(p, s, f, params))
    return results

def randrun(p, s, f, params=()):
    result = None
    if randd() < p:
        result = RunResult(s(*params), True)
    else:
        result = RunResult(f(*params), False)
    return result

def choice(seq):
    return random.choice(seq)

class RunResult:
    __slots__ = ("return_value", "special")
    def __init__(self, return_value, special):
        self.return_value = return_value
        self.special = special

