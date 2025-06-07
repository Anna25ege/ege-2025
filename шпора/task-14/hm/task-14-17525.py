def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 2031):
    num = 3 ** 100 - x
    num_3 = convert(num, 3)
    if num_3.count('0') == 5:
        print(x)
