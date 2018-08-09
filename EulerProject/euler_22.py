import string

letters = string.ascii_uppercase

def get_result():
    total = 0
    with open('./files/p022_names.txt', 'r') as f:
        names = list(f.read().replace('"','').split(','))
    names.sort()
    print(names)
    for pos in range(len(names)):
        score = 0
        for letter in names[pos]:
            score += letters.index(letter) + 1
        total += score * (pos + 1)
    return total