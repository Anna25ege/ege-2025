import string
from itertools import product

alph = '0123456789ABCDEF'

cnt = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('6') == 2:
        for j in '0248ACE':
            i = i.replace(j, '*')
        if '*6' not in i and '6*' not in i and '66' not in i:
            cnt += 1
print(cnt)

