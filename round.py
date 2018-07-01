from jetmath import sort, math

def lrm_round(numbers, total=None):
    if total == None:
        total = 0.0
        for n in numbers:
            total += n
    number_parts = []
    int_sum = 0
    for n in numbers:
        left, right = math.sepd(n)
        number_parts.append([left, right])
        int_sum += left
    number_parts_indices = sort.quicksort(list(range(len(number_parts))), (lambda npi : number_parts[npi][0]), reverse=True)
    for i in range(int(total - int_sum)):
        number_parts[number_parts_indices[i]][0] += 1
    return [i[0] for i in number_parts]

