from itertools import product

alph = sorted('ФОКУС')
cnt = 0

for i in product(alph,repeat=5):
    cnt += 1
    i = ''.join(i)
    if i.count('Ф')==0 and i.count('У') == 2:
        print(cnt,i)