# Определение длины строки
st = 'Hello'
print(len(st))

# Проверка вхождения подстроки в строку
st1 = '5'
st2 = '098764323467'
print(st1 in st2)
print(st1 not in st2)

# Поиск позиции подстроки в строке
st = 'Helle'
print(st.index('ll'))
print(st.find('e'))
print(st.rfind('e'))

# string.split(разделитель sep, кол-во разделений maxsplit)
# Разделяет строку string на подстроки, используя sep как разделитель
# и возвращает список этих подстрок.
# Если параметр sep не указан, то считается, что он равен пробелу.
# Если указан параметр maxsplit, то делается не более maxsplit разбиений
# (т.е. список содержит maxsplit+1 строку).
# Параметр sep может содержать больше одного символа.

st = 'Ivanov Ivan Ivanovich'
print(st.split())

st = '255.255.252.0'
print(st.split('.'))

# join() - возвращает строку, собранную из элементов последовательности
# string.join(iterable)
# применяется к строке string, которая будет вставлена
# между элементами последовательности iterable

client = ['Ivanov', 'Ivan', 'Ivanovich']
print(' '.join(client))

# string.replace(old, new, count)
# Возвращает копию строки string, в которой все элементы old заменены на new
# Параметр count указывает, сколько элементов old необходимо заменить

st = 'boris'
st = st.replace('b', 'B0')
print(st)

# Количество подстрок в строке
st = '09876543456789056789'
print(st.count('0'))




