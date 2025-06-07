def f(A):
    for x in range(1, 1000):
        f = (x % A == 0) or ((70 <= x <= 90) <= (x % 22 != 0))
        if not f:
            return False
    return True


for A in range(1, 1000):
    if f(A):
        print(A)
