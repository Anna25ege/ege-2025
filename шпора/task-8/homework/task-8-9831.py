from itertools import product

alph = '0123456789ABCDEF'

cnt = 0
for i in product(alph, repeat=3):
    i = ''.join(i)
    if i[0] not in '0' and
            cnt += 1
print(cnt)
