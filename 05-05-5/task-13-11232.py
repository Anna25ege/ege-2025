from ipaddress import ip_network

net = ip_network('192.168.31.80/255.255.255.240', False)
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1'):
        cnt += 1
print(cnt)
