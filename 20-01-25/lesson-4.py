
x=int(input())
#Оператор if рабтает с логическим условием.
# Если это условие истино (True), то выполняется блок кода записанный внутри блока if.
# Если условие ложно, то блок if пропускается и
# выполнение кода переходит на следующую после блока if строчку кода.
if x > 0:
    print('+')
#
elif x < 0:
    print('-')
#Чтобы добавить инструкции, которые будут выполняться
# в случае ложного выражения в условии,
# можно использовать оператор else
else:
    print('0')

#Логические операции
# >, <, >=, <=, ==, !=

# not - меняет True на False, и наоборот
num1 = 10
print (not num1)
# and - возвращает True, только тогда,
# когда все значения True
num2 = 10
print(num2 > 0 and num2% 3 == 0)

# or возвращает True, когда хоть бы одно значение True
num3 = 20
print(num3 < 0 or num3 % 2 == 0)

num4 = 52
f1 = num4 % 2 == 0 # True
f2 = num4 == 100 # False
f3 = 10 <= num4 <= 99 # True
if f1 and f2 and f3: #true and false and true -> false
    print('text1')
if f1 or f2 or f3: #true or false or true -> true
    print('text2')
if f1 and f2 or f3: #true and false or true -> true
    print('text3')
if f1 or f2 and f3: # true or false ad true -> true
    print('text4')
if (f1 or f2) and f3 or f1 == f3 or f2:
    # (f1 or f2) and f3 or f1 == f3 or f2
    print('text5')