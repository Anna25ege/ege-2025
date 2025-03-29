from itertools import product, permutations

def f(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d


for a1, a2, a3, a4 in product([0, 1], repeat=4): # считаем пустые клетки (4)
    table = [(a1, a2, 1, a3),# кортеж. расставляем цифры и пустые клетки
             (1, 0, a4, 1),
             (0, 0, 1, 1)]
    if len(table) == len(set(table)): # проверка что все строчки уникальны
        for p in permutations('abcd'):
            u = [f(**dict(zip(p, t))) for t in table] # формирование ответа
            if u == [0, 0, 0]: # из условия. 0 ил 1
                print(*p) # * чтобы были только буквы
