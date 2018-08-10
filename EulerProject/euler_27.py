from my_generators.primes import is_prime

def get_result():
    biggest = 0
    res = ()
    for a in range(-1000,1000):
        for b in range(-1001,1001):
            n = 0
            while True:
                if is_prime(n**2 + a*n + b):
                    n += 1
                else:
                    break
            if n > biggest:
                biggest = n
                res = (a, b)
    return res