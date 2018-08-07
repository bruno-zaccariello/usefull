from EulerProject.my_generators.primes import gen_primes

def get_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 :
            if n/i == i:
                divisors += 1
            else:
                divisors += 2
    return divisors

def get_factors(n):
    factors = {}
    for i in gen_primes(n):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n/i
    return factors