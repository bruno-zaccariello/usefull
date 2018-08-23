from my_generators.primes import gen_primes

# NAO FUNCIONA !!
def get_result():
    n = 1000
    found = False
    while not found:
        a   = gf(n)
        if not a:
            n += 1
            continue

        a1  = gf(n+1)
        if not a1:
            n += 2
            continue

        a2  = gf(n+2)
        if not a2:
            n += 3
            continue

        a3  = gf(n+3)
        if not a3:
            n += 4
            continue

        if a and a1 and a2 and a3:
            return n, n+1, n+2, n+3
        n += 1