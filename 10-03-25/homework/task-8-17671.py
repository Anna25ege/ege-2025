from itertools import product

alph = sorted('ЛАЙМ')

cnt = 0
for i in product(alph,repeat=5):
    i = ''.join(i)
    cnt+=1
    if i.count('М')==0 and i.count('Л')==0 and i.count('ЙЙ')==0:
        print(cnt,i)