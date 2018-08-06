def fibonacci(limit=None):
    a, b = 0, 1
    while True and b < limit :
        yield b
        a, b = b, a+b