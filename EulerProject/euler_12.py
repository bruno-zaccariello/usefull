from my_generators.triangles import triangles
from my_functions.my_math import get_divisors

def get_result():
    for triangle in triangles():
        divisors = len(get_divisors(triangle))
        if divisors > 500:
            return triangle