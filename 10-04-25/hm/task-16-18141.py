from sys import setrecursionlimit


def f(n):
    if n <= 10:
        return n
    if n > 10 and n % 2 == 0:
        return 2 * f(n - 2) + 6
    if n > 10 and n % 2 == 1:
        return f(n - 1) + 2 * n


setrecursionlimit(100000)
print(f(27) - f(20))
