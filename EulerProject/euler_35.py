from my_generators.primes import gen_primes, is_prime
from my_functions.my_math import permutations

def rotate(num):
    for i in range(len(num)-1):
        num = num[-1] + num[:-1]
        yield num

def get_result():
    ans = []
    for i in gen_primes(10**6, start=2):
        circular_prime = True
        for rotation in rotate(str(i)):
            if not is_prime(int(rotation)):
                circular_prime = False
                break
        if circular_prime:
            ans.append(i)
    return ans, len(ans)