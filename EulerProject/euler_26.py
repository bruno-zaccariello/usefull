from my_functions.my_math import decimal_sequence

def get_result():
    max = (1, 1)
    for i in range(1,1000):
        size = len(decimal_sequence(1, i))
        if size > max[0]:
            max = (size, i)
    return max