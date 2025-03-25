for n in range(3,10000):
    st = '1' + '2'*n
    while '12' in st or '32' in st or '22' in st:
        if '12' in st:
            st = st.replace('12','22',1)
        if '32' in st:
            st = st.replace('32','211',1)
        if '22' in st:
            st = st.replace('22','3',1)
    summ=0
    for i in st:
        if sum(map(int,st))%6==0:
            print(n)
            break