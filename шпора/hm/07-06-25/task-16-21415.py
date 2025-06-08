from sys import setrecursionlimit


def f(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + f(n - 2)


setrecursionlimit(3000)

print(f(2126) - f(2122))
