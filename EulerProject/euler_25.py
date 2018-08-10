from my_generators.fibonacci import fibonacci

def get_result():
    count = 0
    for fib in fibonacci():
        count += 1
        if len(str(fib)) >= 1000:
            return count