from itertools import product, permutations


def f(w, x, z, y):
    return (((z == x) <= w) and (w <= (y and x)))


for a1, a2, a3 in product([0, 1], repeat=3):
    table = [(1, 1, a1, 0),
             (1, a2, a3, 0),
             (1, 0, 1, 1)]
    if len(table) == len(set(table)):
        for p in permutations('wxzy'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 1, 1]:
                print(*p)
