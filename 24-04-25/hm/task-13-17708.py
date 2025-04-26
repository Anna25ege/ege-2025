from ipaddress import ip_network

net = ip_network('211.46.0.0/255.255.128.0', False)

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 4 == 0 and i[-1] == '1' and i[-2] == '1':
        cnt += 1
print(cnt)
