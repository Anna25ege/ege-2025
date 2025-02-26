for n in range(3,10000):
    st = '5' +'2'*n
    while '52' in st or '2222' in st or '1122' in st:
        if '52' in st:
            st=st.replace('52','11',1)
        if '2222' in st:
            st=st.replace('2222','5',1)
        if '1122' in st:
            st=st.replace('1122','25',1)
    summ = 0
    for i in st:
        summ = sum(map(int, st))
    if summ == 64:
        print(n)

