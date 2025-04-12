for n in range(4, 10000):
    st = '2' + '7' * n
    while '27' in st or '777' in st or '377' in st:
        if '27' in st:
            st = st.replace('27', '7', 1)
        if '777' in st:
            st = st.replace('777', '3', 1)
        if '377' in st:
            st = st.replace('377', '72',1)
    suma = 0
    mult = 1
    while n > 0:
        digit = n % 10
        suma = suma + digit
        mult = mult * digit
        n = n // 10
        if n % 3 == 0 and str(n)[-1] == '1':
            print(n)
