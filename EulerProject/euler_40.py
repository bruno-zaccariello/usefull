from my_generators.naturals import gen_naturals

def get_result():
    total = 1
    d = 0
    for i in gen_naturals():
        digits = str(i)
        for digit in digits:
            d += 1
            if d in (10, 100, 1000, 10**4, 10**5, 10**6):
                total *= int(digit)
        if d > 10**6:
            break
    return total