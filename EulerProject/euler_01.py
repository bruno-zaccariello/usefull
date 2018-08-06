# Multiplos de 3 e 5 até 1000

# Gerador
def my_generator(limit=None):
    num = 1
    while True and num < limit:
        if num % 3 == 0 or num % 5 == 0:
            yield num
        num += 1

# Pegar o resultado
def get_result():
    soma = 0
    for i in my_generator(1000):
        soma += i
    return soma