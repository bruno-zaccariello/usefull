def fibonacci(limit=None):
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            break
        yield b
        a, b = b, a+b