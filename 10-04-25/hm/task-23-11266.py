def f(cur,end):
    if cur == end:
        return 1
    if cur <end or cur == 11:
        return 0
    return f(cur//3,end) + f(cur-1,end) + f(cur-2,end)

print(f(30,8))