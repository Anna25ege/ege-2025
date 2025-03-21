# срезы

st = 'hello stepan'
# Если мы хотим извлечь один элемент строки/списка,
# то после названия переменной в квадратных скобках
# ставим номер позиций интересующего нас элементы
# Нумерация всегда начинается с нуля и действует слева направо
print(st[4])

# Существует обратная нумерация
# Она начинается с -1 и действует справа налево
print(st[-2])

print(st[-6:])

# срез реализуется при помощи знака :
#см срез в тг
print(st[::2])
# 2 = шаг

arr = 'Hello World!'

# 1. Перевернуть список
print(arr[::-1]) # переворот
# 2. Вывести каждую вторую букву
print(arr[::2])
# 3. Вывести каждую третью букву первого слова
print(arr[:5:3])
# 4. Вывести второе слово перевернутым
print(arr[-6::][::-1])
# 5. Вывести каждую вторую букву перевернутого строки целиком
print(arr[::-1][::2])

