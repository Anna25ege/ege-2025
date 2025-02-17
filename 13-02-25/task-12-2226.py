st='300'+'8'
while '555' in st or '888' in st:
    if '555' in st:
        st =st.replace('555','8',1)
    else:
        st= st.replace('888','55',1)
a1 = '5'
a2 = '8'
print(a1 and a2 in st)
print(st)