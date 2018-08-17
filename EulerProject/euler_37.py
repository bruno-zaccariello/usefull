from my_generators.primes import gen_primes, is_prime

def get_result():
    ans = []
    for i in gen_primes(start=10):
        r, l = str(i), str(i)
        truncatable = True
        while len(l) > 1 and len(r) > 1:
            l, r = l[1:], r[:-1]
            if not is_prime(int(l)) or not is_prime(int(r)):
                truncatable = False
                break
        if truncatable:
            ans.append(i)
            if len(ans) >= 11:
                return ans, sum(ans)