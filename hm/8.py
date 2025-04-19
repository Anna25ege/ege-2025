from itertools import product

alph = '012345678'

cnt = 0
for i in product(alph, repeat=7):
    i = ''.join(i)
    if i[0] != '0' and i[-1] != '3' and i[-1] != '4' and i[-1] != '7' \
            and i.count('000') + i.count('111') + i.count('222') \
            + i.count('333') + i.count('444') + i.count('555') \
            + i.count('666') + i.count('777') + i.count('888') == 0:
        cnt +=1
        print(cnt)
