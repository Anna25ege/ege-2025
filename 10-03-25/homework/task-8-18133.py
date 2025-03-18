from itertools import product

alph = sorted('КОДИМ')
cnt = 0

for i in product(alph,repeat=5):
    i = ''.join(i)
    cnt += 1
    if i.count('М') == 2 and i.count('ММ')==0:
        print(cnt,i)