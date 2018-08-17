def is_prime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** (0.5)) + 1, 2):
            if n % i == 0:
                return False
        return True
    else:
        return False

def gen_primes(limit=None, start=1):
    num = start
    while True:
        if limit and num > limit:
            break
        if is_prime(num):
            yield num
        num += 1