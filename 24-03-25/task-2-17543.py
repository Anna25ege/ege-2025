from itertools import product, permutations


def f(w, z, x, y):
    return ((y <= ((not (x <= z)))) or w)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, 0, a2, a3),
             (0, 1, a3, a4),
             (1, a5, a6, 0)]
    if len(table) == len(set(table)):
        for p in permutations('wzxy'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)
