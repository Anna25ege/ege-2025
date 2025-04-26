from ipaddress import ip_network

net = ip_network('122.159.136.144/255.255.255.248')

cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 4 != 0:
        cnt += 1
print(cnt)
