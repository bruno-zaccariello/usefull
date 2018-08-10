from my_functions.my_math import FNS

def get_result():
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Pos 10**6 is actually 10**6 - 1 (due to 0 index)
    # Get factoradic number of 999.999
    fns = FNS((10**6)-1)
    result = ''
    # Transform the factoradic to positional combination
    for pos in fns:
        result += chars.pop(int(pos))
    return result