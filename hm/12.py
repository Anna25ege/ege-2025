st = '1' + '0' * 90

while '1' in st:
    if '10' in st:
        st = st.replace('10', '0001')
    else:
        st = st.replace('1', '000')
        print(st.count('0'))
