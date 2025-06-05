from itertools import product

alph = sorted('ПОБЕДА')

cnt = 0

for i in product(alph, repeat=6):
    i = ''.join(i)
    cnt += 1
    if cnt % 2 == 0 and i[0] == 'О' and i.count('П') == i.count('О') == i.count('Б') == \
            i.count('Е') == i.count('Д') == i.count('А') == 1:
        print(cnt)
