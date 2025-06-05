from itertools import product

alph = sorted('мангуст')

cnt = 0

for i in product(alph, repeat=6):
    i = ''.join(i)
    cnt += 1
    if i[0] not in 'у' and i.count('м') == 2 and i.count('г') <= 1:
        print(cnt)
