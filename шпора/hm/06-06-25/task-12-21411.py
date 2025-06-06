for n in range(4, 10000):
    st = '3' + '1' * n
    while '31' in st or '211' in st or '1111' in st:
        if '31' in st:
            st = st.replace('31', '1', 1)
        if '211' in st:
            st = st.replace('211', '13', 1)
        if '1111' in st:
            st = st.replace('1111', '2', 1)
    summ = 0
    for i in st:
        summ = sum(map(int, st))
    if summ == 15:
        print(n)
        break
