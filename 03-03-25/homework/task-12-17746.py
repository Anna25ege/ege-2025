for n in range(1,10000):
    st = '9'*68
    while '22222' in st or '9999' in st:
        if '22222' in st:
            st = st.replace('22222','99',1)
        else:
            st =st.replace('9999','29',1)

    if st.count('9'):
        print(st)
