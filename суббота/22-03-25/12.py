for n in range(1,10000):
    st = '9' + '6'*n
    while '96' in st or '6666' in st or '1166' in st:
        if '96' in st:
            st=st.replace('96','11',1)
        if '6666' in st:
            st=st.replace('6666','9',1)
        if '1166' in st:
            st=st.replace('1166','69',1)
    summ = 0
    for i in st:
        summ = sum(map(int, st))
        if summ == 37:
            print(n)