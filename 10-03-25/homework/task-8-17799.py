from itertools import product

alph = sorted('аргумент')
cnt = 0

for i in product(alph,repeat=4):
    i = ''.join(i)
    cnt += 1
    if len(i) == len(set(i)):
        if list(i) == sorted(i):
            print(cnt)


