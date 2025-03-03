from string import digits, ascii_uppercase

alph= digits + ascii_uppercase

for x in alph[:24]:
    num1 = int('12' + x + '734', 24)
    num2 = int('8'+ x + '95' + x + '3',24)
    num3 = int('24' + x + '796', 24)
    num = num1 + num2 + num3
    if num % 23 == 0:
        print(num//23)


