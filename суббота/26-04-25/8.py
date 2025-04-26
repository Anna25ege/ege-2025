from itertools import product

cnt = 0

for i in product((sorted('ПОБЕДА')), repeat=6):
    i = ''.join(i)
    cnt += 1
    if cnt % 2 == 0 and i[0] == 'О' and i.count('П') == i.count('О') == i.count('Б') == \
            i.count('Е') == i.count('Д') == i.count('А') == 1:
        if len(i)==len(set(i)):
            print(cnt)
