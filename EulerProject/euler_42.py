import string
from my_generators.triangles import triangles

lts = string.ascii_uppercase
l = {}

j = 1
for i in lts:
    l[i] = j
    j += 1

def get_result():
    total = 0
    with open('./files/p042_words.txt') as f:
        words = list(f.read().replace('"', '').split(','))
    for word in words:
        _sum = 0
        for letter in word:
            _sum += l[letter]
        for t in triangles(t_limit=_sum+1):
            if t == _sum:
                total += 1
                break
    return total