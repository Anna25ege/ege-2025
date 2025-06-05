from itertools import product

alph = '01234567'

wrong_pairs = {'16', '36', '56', '67',
               '61', '63', '65', '76'}
cnt = 0

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in '0' and i.count('6') == 1 and all(pair not in i for pair in wrong_pairs):
        cnt += 1
        print(cnt)
