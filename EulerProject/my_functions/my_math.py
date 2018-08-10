from EulerProject.my_generators.primes import gen_primes
from itertools import count

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 :
            if n/i == i:
                divisors += [i]
            else:
                divisors += [i, int(n/i)]
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

def permutations(sequence):
    if len(sequence) <= 1:
        yield sequence
    else:
        for perm in permutations(sequence[1:]):
            for index in range(len(perm)+1):
                yield perm[:index] + sequence[0] + perm[index:]

def FNS(n):
    quotient = n
    coefficients = []
    radix = 1
    while quotient != 0:
        quotient, remainder = divmod(quotient, radix)
        coefficients.append(remainder)
        radix += 1
    return ''.join(str(x) for x in coefficients[::-1])

def decimal_sequence(d, number):
    repeating = []
    gone_dividends = [d]
    dividend = d
    while dividend:
        # Get the actual numer of the division result
        actual = dividend // number

        # Add it to the result
        repeating.append(actual)

        # get the new dividend
        dividend = dividend % number * 10

        # If it's not done yet add to the dones
        if dividend not in gone_dividends:
            gone_dividends.append(dividend)
        # Else we found the end of the repeating process
        else:
            break

    size = len(repeating)
    if size > 1:
        # Get the actual sequence
        actual = dividend // number
        next = (dividend % number * 10)//number
        for i in range(len(repeating[1:])):
            if repeating[i] == actual and repeating[i+1] == next:
                repeating = repeating[i:]
                break
    return repeating