from my_functions.my_math import factorial

def get_result():
    chars = [int(x) for x in str(factorial(100))]
    return sum(chars)