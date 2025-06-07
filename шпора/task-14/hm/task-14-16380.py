def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024

num_25 = convert(num, 25)
cnt = 0
while num:
    if num % 25 > 10:
        cnt += 1
    num //= 25
print(cnt)
