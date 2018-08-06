from my_generators.primes import gen_primes


soma = 0
for i in gen_primes(2 * (10 ** 6)):
    soma += i
print(f'result: {soma}')