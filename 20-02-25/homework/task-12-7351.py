st = '7'*512
count=0
while '7777' in st or '1111' in st:
    if '7777' in st:
            st = st.replace('7777','1',1)
            count += 1
    else:
            st = st.replace('1111','7',1)
            count += 1
print(count)
