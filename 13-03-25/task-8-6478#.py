from itertools import product

cnt = 0
for i in product('МОЛЬ', repeat=5):
    i= ''.join(i)
    if i.count('МЬ')and i.count('ЛЬ'):
        cnt += 1
        print(cnt,i)

