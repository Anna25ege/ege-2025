from sys import setrecursionlimit

def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + f(n - 1)

setrecursionlimit(2100)
print(f(2024) - f(2021))
