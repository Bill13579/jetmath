from jetm import random, math

def quicksort(arr, get_comparable_value=math.identity):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    pivit = random.randint(0, len(arr)-1)
    pivit_ele = arr[pivit]
    left = []
    right = []
    for e in (arr[:pivit] + arr[pivit+1:]):
        if get_comparable_value(e) < get_comparable_value(pivit_ele):
            left.append(e)
        else:
            right.append(e)
    return quicksort(left, get_comparable_value) + [pivit_ele] + quicksort(right, get_comparable_value)

