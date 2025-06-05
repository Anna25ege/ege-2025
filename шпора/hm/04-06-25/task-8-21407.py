from itertools import product

alph = sorted('ДГИАШЭ')

cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in 'ИАЭ' and i[-1] not in 'ДГШ':
        cnt += 1
print(cnt)
