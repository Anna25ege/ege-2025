from itertools import product

alph = sorted('СЕНТЯБРЬ')

cnt = 0
for i in product(alph,repeat=5):
    i =''.join(i)
    cnt+=1
    if cnt % 2 ==0 and i[0]=='Р' and i.count('Ь')==0:
        print(cnt,i)
