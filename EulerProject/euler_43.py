from my_functions.my_math import permutations

def get_result():
    total = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]

    # Gets all the pandigital 0 to 9
    # First if to ignore left zeros
    for p in permutations('0123456789'):
        if p.startswith('0'):
            continue

        # Setup a control for slicing the str
        # And one to check if we show add it
        c = 1
        add = True
        for d in divisors:
            if int(p[c:c+3]) % d != 0:  # Checks if any 3-piece
                add = False             # substring is divisable by the actual divisor
                break
            c += 1
        total += int(p) if add else 0

    return total