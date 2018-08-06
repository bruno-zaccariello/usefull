# Achar a diferença entre a soma das potências dos números de 1-100 e a potência da soma dos números de 1-100

def get_result():
    total = sum(range(1, 101))**2 - sum([x**2 for x in range(1,101)])
    return total