interfaces = {
    'eth0' : {'IP Address': '1.1.1.1', 'status': 'up'},
    'eth1' : {'IP Address': '2.2.2.2', 'status': 'up'},
    'wlan0': {'IP Address': '3.3.3.3', 'status': 'down'},
    'wlan1': {'IP Address': '4.4.4.4', 'status': 'up'}
}

# status = interfaces['eth0']['status']
# print(status)

for interface, details in interfaces.items():
    if details['status'] == 'up':
        print(f'{interface} : {details["IP Address"]}')

totallen = len(interfaces)
print(totallen)

add = {"IP Address": '5.5.5.5', 'status':'down'}