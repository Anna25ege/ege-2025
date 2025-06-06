for n in range(4, 10000):
    st = '4' + '2' * n
    while '42' in st or '8222' in st or '2222' in st:
        if '42' in st:
            st = st.replace('42', '2', 1)
        if '8222' in st:
            st = st.replace('8222', '24', 1)
        if '2222' in st:
            st = st.replace('2222', '8', 1)
    summ = 0
    for i in st:
        summ = sum(map(int, st))
    if summ == 110:
        print(n)
        break
