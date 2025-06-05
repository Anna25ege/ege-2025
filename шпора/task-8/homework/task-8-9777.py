from itertools import product

alph = sorted('компьютер')

cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    cnt += 1
    if cnt % 2 != 0 and i[0] not in 'ь' and i.count('к') == 2:
        print(cnt)
