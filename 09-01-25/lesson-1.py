"""print("Hello world")
print("ofojfojfdbop")"""

var_int = 10
var_float = 5.5
var_str = '10'
var_list = [4, 6, 3, 'Privet', 6.9]
var_tuple = (9, 7, 'priv', 14.89)
var_set = {'name':'test','age':15}
var_bool = True

print(var_int + int(var_str))

str_1 = 'Hello '
str_2 = 'world'
print(str_1+str_2)

str_1 = 'hello user'
id = 567
print(str_1 + str(id))


#Приведение типов данных необходимо для преобразования
# одного типа в другой, чтобы появилась возможность
# выполнять действия с нужным типом

#Преобразование типов осуществляется за счет вызова функции,
# название которой совпадает с названием типа данных

# Пример 1 ( нельзя суммировать числа и строки. Поэтому мы превращаем строку в число
# при помощи команды int()):
num_1 = 100
str_1 = '200'
print(num_1 + int(str_1))

# Пример 2 (нельзя приписать число к строке. Поэтому мы превращаем число в строку
# при помощи команды st()):
welcome_text = 'Hello User'
id = 1
print(welcome_text + str(id))