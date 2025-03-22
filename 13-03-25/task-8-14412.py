from itertools import product
# нет alph потому что не указано что по порядку
cnt = 0
for i in product('АЛГОРИТМ', repeat=6):
    i = ''.join(i)
    if i.count('Л') <= 1 and i[0] != 'Р' and i[-1] in 'АОИ':
        cnt += 1

print(cnt)
# л не болеее одного раза
# слово не оканчивается на согласные