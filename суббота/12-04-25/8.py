from itertools import product

alph = sorted('МИЗАНТРОП')

cnt = 0
for i in product(alph,repeat=5):
    i = ''.join(i)
    cnt += 1
    if cnt % 2 == 0 and i[0] == 'Н' and i.count('Р') == 2:
        print(cnt)