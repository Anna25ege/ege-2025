# функция для перевода любого числа в указанную систему счисления (2 <= sys <=)
def convert(num,sys): # num число, sys= система счисления
    res= '' #res=строка
    while num!= 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

# Перевод в двоичную систему счисления (результата приходит в виде строки)
print(bin(17), convert(17,2))
# Перевод в восьмеричную систему счисления (результата приходит в виде строки)
print(oct(17), convert(17,8))
# Перевод в шестнадцатеричную систему счисления (результата приходит в виде строки)
print(hex(17), convert(17,16))