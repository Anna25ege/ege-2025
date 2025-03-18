from itertools import product

alph=sorted('ИГРОК')

cnt = 0

for i in product(alph,repeat=5):
    i = ''.join(i)
    if i.count('И')<=1 and i.count('Г')<=1 and i.count('Р')<=1 and  i.count('О')<=1 and i.count('К')<=1 and i[0]!='К' and i.count('РОК')==0:
        cnt+=1
        print(cnt,i)