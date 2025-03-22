from itertools import product

alph = sorted(set('СУБЛИМАЦИЯ'))

cnt=0

for i in product(alph,repeat=5):
    cnt += 1
    i = ''.join(i)
    if cnt % 2 != 0 and i [-1] != 'Я' and \
            i.count('У') + i.count('И') + i.count('А') + i.count('Я')== 2:
        print(cnt)