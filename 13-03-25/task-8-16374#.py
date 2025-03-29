from itertools import product

alph='0123456'
cnt = 0
for i in product(alph, repeat=7):
    i = ''.join(i)
    if i[0]!=0 and  i.count('2') + i.count('4') + i.count('6') == 2:
        cnt += 1
        print(cnt)
