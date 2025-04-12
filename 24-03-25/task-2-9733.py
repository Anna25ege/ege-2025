from itertools import product, permutations


def f(w, y, x, z):
    return ((x and (not y)) or ((x == z)) or w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, a2, 0, 1),
             (1, 0, a3, 1),
             (1, 1, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations('wyxz'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)
