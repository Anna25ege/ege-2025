from sys import setrecursionlimit

def F(n):
    if n < 100:
        return n ** 2
    if n > 99 and n % 2 == 0:
        return 0.5 * F(n - 1)
    if n > 99 and n%2 ==1:
        return 2 * F(n-1)

setrecursionlimit(16400)

print(1000 * F(16384) / F(7777))