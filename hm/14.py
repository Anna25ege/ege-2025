def convert(num, sys):
    res = []
    while num:
        res = str(num % sys)
        num //= sys
    return res[::-1]


for x in range(2, 2026):
    num = 5 ** 2025 + 5 ** 200 - x
    nun = convert(num, 5)
    if num.count('4'):
        print(x)
