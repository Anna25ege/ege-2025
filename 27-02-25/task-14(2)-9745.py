from string import digits, ascii_uppercase

alph = digits + ascii_uppercase #36 символов

for x in alph[:19]: # alph 19 системы
    num1 = int('98' + x + '79641',19)
    num2 = int('36'+ x + '14',19)
    num3 = int('73' + x + '4',19)
    num = num1 + num2 + num3
    if num % 18 ==0:
        print(num//18)

def sum_digits(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s
