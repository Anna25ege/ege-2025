# нащлось
a1 = '1'
a2 = '1234'
print(a1 in a2)

# заменить все вхождения
st = '12341234'
st = st.replace('1','*')
print(st)

# заменить один раз
st = '12341234'
st = st.replace('1','*',1)
print(st)

# формирование строки нудной длины

st = '1' * 100
print(st)

#сумма цифр числа

#способ 1
summ = 0
for i in st:
    summ += int(i)

#способ 2
summ = sum(int(i) for i in st)

#способ 3
summ = sum(map(int, st))