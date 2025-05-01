from itertools import product

alph = '01234567'
cnt =0
for i in product(alph,repeat=5):
    i = ''.join(i)
    if i[0]!=0 and i.count('6')==1 and i.replace('6','*',):
        if i.count('*6')==0 and i.count('6*')==0:
            cnt +=1
print(cnt)

