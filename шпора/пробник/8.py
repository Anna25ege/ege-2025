from itertools import product

alph = '0123456789AB'

cnt = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in '0' and i.count('7') == 1:
        if i.count('9') + i.count('A') + i.count('B') <= 3:
            cnt += 1
print(cnt)
