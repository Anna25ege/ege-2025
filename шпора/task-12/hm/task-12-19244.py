for n in range(4, 10000):
    st = '1' + '2' * n
    while '12' in st or '322' in st or '222':
        if '12' in st:
            st = st.replace('12', '2', 1)
        if '322' in st:
            st = st.replace('322', '21', 1)
        if '222' in st:
            st = st.replace('222', '3', 1)
    summ = 0
    for i in st:
        summ = sum(map(int, st))
    if summ == 15:
        print(n)
        break
