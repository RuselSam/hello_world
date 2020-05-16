mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':','.')
print(mac)

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlans = config.split()[-1].split(',')
print(vlans)

vlans1 = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans1.sort()
vlans_sorted = set(vlans1)
print(vlans_sorted)

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
vlans2 = set(command1.split()[-1].split(',')) & set(command2.split()[-1].split(','))
print(vlans2)

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
ospf_route[0] = 'OSPF'
ospf_route.pop(3)
d1 = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
new_dict = dict.fromkeys(d1)
list4 = list(new_dict)
x = 0
y = 0
while(x < len(new_dict)):
    if x <= (len(new_dict)-1) and y <= (len(ospf_route)-1):
        m = ospf_route[y]
        m = str(m)
        new_dict[list4[x]] = m
        x += 1
        y += 1
    else:
        break
print(new_dict)

mac = 'AAAA:BBBB:CCCC'
mac = mac.lower().split(':')
mac = mac[0]+mac[1]+mac[2]
mac = int(mac, 16)
print(f'{mac:b}')

ip = '192.168.3.1'
ip = ip.split('.')
i = 0
for i in range(len(ip)):
    print(type(ip[i]))
    ip[i] = int(ip[i])
    print(type(ip[i]))

"""while i < len(ip):
    if i <= (len(ip)-1):
        print(type(ip[i]))
        ip[i] = int(ip[i])
        print(type(ip[i]))
        i += 1
    else:
        break
"""
print(f'''
      {ip[0]:<8} {ip[1]:<8} {ip[2]:<8} {ip[3]:<8}
      {ip[0]:08b} {ip[1]:08b} {ip[2]:08b} {ip[3]:08b}''')


