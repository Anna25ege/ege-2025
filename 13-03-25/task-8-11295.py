from itertools import product

alph=sorted('ЩЭДСР')

cnt = 0

for i in product(alph,repeat=4):
    cnt+=1
    i=''.join(i)
    if i.count('ЩДЩД'):
        print(cnt,i)