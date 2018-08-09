def permutations(sequence):
    if len(sequence) <= 1:
        yield sequence
    else:
        for perm in permutations(sequence[1:]):
            for index in range(len(perm)+1):
                yield perm[:index] + sequence[0] + perm[index:]