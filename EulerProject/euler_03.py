# Maior número da fatoração do numero 600851475143

from my_generators.primes import gen_primes

def get_result():
    num = 600851475143
    for i in gen_primes():
        while num % i == 0:
            num = num/i
        max = i
        if num <= 1:
            break
    return(max)