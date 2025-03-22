from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:25]:
    num1 = int('A4' + x + '7F2', 25)
    num2 = int('N' + x + 'G5' + x + 'H', 25)
    num3 = int('74' + x + 'M26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        print(num // 24)
