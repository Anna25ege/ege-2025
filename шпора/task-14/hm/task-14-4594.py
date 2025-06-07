def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 4 * 625 ** 1920 + 4 * 125 ** 1930 - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960

num_5 = convert(num, 5)
print(num_5.count('0'))
