def f(cur, end):
    if cur == end:
        return 1
    if cur > end:
        return 0
    return f(cur + 1, end) + f(cur + 2, end) + f(cur * 2, end)


print(f(4, 11) * f(11, 13) * f(13, 15))
