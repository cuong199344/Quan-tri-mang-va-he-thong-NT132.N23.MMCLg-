from netmiko import ConnectHandler

my_device = ['192.168.1.62','192.168.1.61','192.168.1.60']
device_list = list()

for device_ip in my_device:
    device = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': 'admin',
        'password': 'netmiko',
        'secret': 'cisco'
    }
    device_list.append(device)   

config_commands = ['access-list 5 permit host 1.1.1.1', 'ntp server 192.167.1.1' ]

for each_device in device_list:
    connect = ConnectHandler(**each_device)
    connect.enable()
    print(f'Connecting to {each_device["ip"]}')
    output = connect.send_config_set(config_commands)
    print(output)
    print(f'Closing Connection on {each_device["ip"]}')
    connect.disconnect()
    


