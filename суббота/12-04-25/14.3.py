def convert(num, sys):
    res = []
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 10000):
    num = 3 * 2000 + 3 ** 10 - x
    ans = convert(num, 3)
    if ans.count('2') == 2000:
        print(x)
        break
