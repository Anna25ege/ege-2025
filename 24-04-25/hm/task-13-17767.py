from ipaddress import ip_network

net = ip_network('228.172.236.0/255.255.240.0',False)

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 5 != 0:
        cnt += 1
print(cnt)
