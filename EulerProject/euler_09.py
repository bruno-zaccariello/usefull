# Achar o trio de número pitágoricos que somados dá 1000 (a² + b² = c² e a+b+c=1000)

def get_result():
    for a in range(2,998,2):
        for b in range(3,999,3):
            for c in range(5, 1001, 5):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c, a*b*c