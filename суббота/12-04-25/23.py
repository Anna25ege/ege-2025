def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 35:
        return 0
    return f(cur + 1, end) + f(cur + 2, end) + (cur * 2, end)


print(f(7, 13) * f(13, 15) * f(15, 51))
