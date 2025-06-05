from itertools import product

alph = '012345678'

wrong_pairs = {'10', '30', '50', '70',
               '01', '03', '05', '07'}

cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in '0' and i.count('0') == 1 and all(pair not in i for pair in wrong_pairs):
        cnt += 1
        print(cnt)
