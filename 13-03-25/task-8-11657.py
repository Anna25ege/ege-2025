from itertools import product
cnt = 0
alph = '01234567'

for i in product(alph,repeat=6):
    i = ''.join(i)
    cnt +=1
    if i [0] != '0' and i.count('3')==0 and len(i) == len(set(i)) and i.count('24') +\
         + i.count('42') and i.count('26') + i.count('62') +\
            + i.count('36') + i.count('63') <=1:
        print(cnt)


