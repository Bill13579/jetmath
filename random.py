import random
from jetm import matrix

def seed(seed):
    random.seed(random.SystemRandom().randint(0, 2147483647))

def rand(rows, cols):
    m = matrix.zeros(rows, cols)
    for r in range(m.shape[0]):
        for c in range(m.shape[1]):
            m[r,c] = randd()
    return m

def uniform(start, end):
    return random.uniform(start, end)

def randd():
    return random.uniform(-1.0, 1.0)

def happened(event):
    if uniform(0, 1) < event:
        return True
    else:
        return False

def randruns(p, s, f, params=(), iterations=1):
    results = []
    for i in range(iterations):
        results.append(randrun(p, s, f, params))
    return results

def randrun(p, s, f, params=()):
    result = None
    if uniform(0, 1) < p:
        result = RunResult(s(*params), True)
    else:
        result = RunResult(f(*params), False)
    return result

def choice(seq):
    return random.choice(seq)

def probchoice(seq, probabilities, total_prob=1):
    if total_prob == None:
        total_prob = 0.0
        for prob in probabilities:
            total_prob += prob
    running_sum = 0.0
    c = uniform(0, total_prob)
    for i in range(len(seq)):
        running_sum += probabilities[i]
        if c < running_sum:
            return seq[i]

class RunResult:
    __slots__ = ("return_value", "special")
    def __init__(self, return_value, special):
        self.return_value = return_value
        self.special = special

