import string
from itertools import product

alph= string.printable[:15]

cnt = 0
for i in product(alph,repeat=5):
    i = ''.join(i)
    if i[0]!='0' and i.count('8')==1 and \
            i.count('a') + i.count('b') + i.count('c') + i.count('d') + i.count('e') >=2:
        cnt +=1
print(cnt)

