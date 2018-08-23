def gen_naturals(limit=None):
    i = 1
    while True:
        if limit and i >= limit:
            break
        yield i
        i += 1