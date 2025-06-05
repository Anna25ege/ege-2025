from itertools import product

alph = sorted('ГЕПАРД')

cnt = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i.count('Г') == 1 and i[0] not in 'А' and i[-1] not in 'Е':
        cnt += 1
print(cnt)
