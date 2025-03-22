from itertools import product

alph=('01234567')
cnt=0
c1='0246'
c2='1357'
for i in product(alph, repeat=5):
    s=''.join(i)
    if i[0]!='0':
        if len(i)==len(set(i)) and i.count('1')==0:
            if s in c1 and s in c1 or s in c2 and s in c2:
                break
            else:
                if s[0] != '0':
                    cnt += 1
        print(cnt)
