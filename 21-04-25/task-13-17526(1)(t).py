from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0')  # ip  и маска

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 2 != 0:
        cnt += 1
print(cnt)

from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0')

net.network_address # адрес сети
net.broadcast_address # широковещательный адрес
net.netmask # маска сети
net.num_addresses # кол-во IP адресов
net.hosts() # узлы сети

