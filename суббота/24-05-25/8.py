from itertools import product

cnt = 0
for i in product((sorted('ПАРУС')), repeat=5):
    i = ''.join(i)
    cnt += 1
    if i.count('У') <= 1 and i.count('АА') == 0:
        print(cnt)
