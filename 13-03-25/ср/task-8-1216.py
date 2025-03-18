from itertools import product

alph=('01234')

cnt =0
for i in product(alph,repeat=6):
    i =''.join(i)
    cnt += 1
    if i[0]!='1' and i[-1]!='3' and '4':
        print(cnt,i)