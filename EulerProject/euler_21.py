from my_functions.my_math import get_divisors

def gen_numbers(limit=None):
    i = 0
    while True:
        if i > limit:
            break
        i += 1
        yield i

def get_result():
    amicables = []
    for a in gen_numbers(10000):
        b = sum(get_divisors(a))-a
        if sum(get_divisors(b))-b == a and a != b:
            if a not in amicables or b not in amicables:
                amicables += [a, b]
    return sum(amicables)