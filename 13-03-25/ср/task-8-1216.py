from itertools import product

alph=('01234')

cnt =0
for i in product(alph,repeat=6):
    i =''.join(i)
    if i[0]!='1' and i[-1]!='3' and i[-1]!='4':
        cnt+=1
        print(cnt,i)