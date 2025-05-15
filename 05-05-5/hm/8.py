from itertools import product

alph = (0,1,2,3,4)

cnt = 0
for i in product(alph, repeat=6):
    if sum(i) % 2 == 0 and i[0] == 3:
        cnt += 1
print(cnt)
