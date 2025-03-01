num = int(input('Введите трехзначное число:'))

852

r1 = num % 10
r2 = num // 10 % 10
r3 = num // 100

print(r1, r2, r3)
