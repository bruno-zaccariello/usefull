from my_generators.primes import is_prime
from my_functions.my_math import permutations

def get_perms(string):
    for p in permutations(string):
        yield p

def get_result():
    largest = 0
    pandigital = '123456789'

    # We start from the highest possibilities of pandigitals
    # and while not found a prime we go going for lower
    # pandigitals
    found = False
    while not found:
        for number in get_perms(pandigital):
            n = int(number)
            print(n, is_prime(n))
            if is_prime(n) and n > largest:
                largest = n
                found = True
        pandigital = pandigital[:-1]
    return largest