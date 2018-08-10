from EulerProject.my_generators.primes import gen_primes

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 :
            if n/i == i:
                divisors += [i]
            else:
                divisors += [i, n/i]
    return divisors

def get_divisors_sum(n):
    divisors_sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                divisors_sum += i
            else:
                divisors_sum += i + (n / i)
    return divisors_sum-n

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

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def FNS(n):
    mks = []
    factor = 2
    while n > 1:
        print(n, factor, n % factor, n // factor)
        if factor == 2:
            mks.append(str(1))
        else:
            mks.append(str(n%factor))
        n = n//factor
        factor += 1
    return ''.join(mks[::-1])