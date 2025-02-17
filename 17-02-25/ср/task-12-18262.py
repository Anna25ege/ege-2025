for n in range(1,1000):
    st = '>'+'0'*17 + '3'*n + '2'*17
    while '>3' in st or '>2' in st or '>0' in st:
        if '>3' in st:
            st = st.replace('>3','22>',1)
        if '>2' in st:
            st = st.replace(">2",'2>',1)
        if '>0' in st:
            st=st.replace('>0','3>',1)

    summ = sum(map(int,st[:-1]))
    if summ **0.5==int(summ**0.5):
        print(n)
        break


