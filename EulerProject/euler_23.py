from my_functions.my_math import get_divisors_sum as D

def make_abundant_list():
    MAX = 28124
    abundant = []
    i = 0
    while True:

        # Check limit
        i += 1
        if i >= MAX:
            break

        # Get number divisor sum
        res = D(i)

        # Check if is abundant
        if res > i:
            abundant.append((i, res))
    ab_sums = [False] * MAX
    for i in abundant:
        for j in abundant:
            if i[0]+j[0] < MAX:
                ab_sums[i[0]+j[0]] = True
    return abundant, ab_sums

def get_result():
    abundant = make_abundant_list()
    ans = sum([i for (i, x) in enumerate(abundant[1]) if not x])
    return ans