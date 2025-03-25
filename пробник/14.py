def convert(num,sys):
    res =''
    while num:
        res += str(num%sys)
        num//= sys
    return res [::-1]

for x in range(1,2030):
    num1 = 2**2025 + 2**2024 - 2**2021 - x
    num2 = convert(num1,4)
    num3 = num2.count('0')
    print(x)


