def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
cnt = 0
num_9 = convert(num, 9)
while num:
    if num % 9 != 0:
        cnt += 1
    num = num // 9
print(cnt)
