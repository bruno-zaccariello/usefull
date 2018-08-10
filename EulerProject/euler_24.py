from my_functions.my_math import FNS

def permutations(sequence):
    if len(sequence) <= 1:
        yield sequence
    else:
        for perm in permutations(sequence[1:]):
            for index in range(len(perm)+1):
                yield perm[:index] + sequence[0] + perm[index:]

def get_result():
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    fns = FNS(10**6)
    print(fns)
    result = ''
    for pos in fns:
        result += chars.pop(int(pos))
        print(pos, result, chars)
    return result