from itertools import product

alph = ('012345678')

cnt = 0
for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('5') == 1 and '11' not in i and '22' not in i and '33' not in i and '44' not in i \
            and '55' not in i and '66' not in i and '77' not in i and '88' not in i:
        cnt +=1
print(cnt)
