# Soma dos números pares em uma sequência de fibonacci até 4 milhões

from my_generators.fibonacci import *

# Se o número na sequência for par adiciona na soma.
def get_result():
    soma = 0
    for i in fibonacci(4*(10**6)):
        if i % 2 == 0:
            soma += i
    return soma