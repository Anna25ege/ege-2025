from itertools import product
alph = "0123456789AB"

cnt=0
for i in product(alph,repeat=7):
    i=''.join(i)
    cnt+=1
    if i.count('BB')==1 and
