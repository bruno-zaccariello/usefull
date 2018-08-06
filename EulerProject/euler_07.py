# Achar o número primo de número 10001

from my_generators.primes import gen_primes

def get_result():
    iter = 0
    for i in gen_primes():
        iter += 1
        if iter == 10001:
            return i