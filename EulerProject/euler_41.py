from my_generators.primes import is_prime
from my_functions.my_math import permutations

def get_result():
    largest = 0
    for number in permutations('1234567'):
        n = int(number)
        print(n, is_prime(n))
        if is_prime(n) and n > largest:
            largest = n
    return largest