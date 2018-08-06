# Achar o maior número palíndromo resultado de uma multiplicação entre dois números com 3 digitos.

# Função para testar se é palíndromo
def is_palindrome(word):
    word = str(word)
    if len(str(word)) <= 1:
        return True
    if str(word)[0] == str(word)[-1]:
        return is_palindrome(word[1:-1])
    return False

# Retorna uma tupla com o maior valor e os números que multiplicam para chegar nele
def get_result():
    max = [0]
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            product = i*j
            if is_palindrome(product):
                if product > max[0]:
                    max = product, i, j
    return max