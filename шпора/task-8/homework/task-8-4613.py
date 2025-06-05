from itertools import product

alph = '012345678'

cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in '01357' and i[-1] not in '18' and  i.count('3') <= 1:
        cnt += 1
        print(cnt)
