def F(current, end):
    if current == end:
        return 1
    if current > end or current == 12:
        return 0
    return F(current + 1, end) + F(current + 2,end) + F(current * 3, end)

print(F(2,9) * F(9,19))