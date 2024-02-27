from netmiko import ConnectHandler

device = ["192.168.1.62","192.168.1.61","192.168.1.60"]
device_List = list()

for device_ip in device:
    Router = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": "admin",
        "password": "netmiko",
        "secret": "cisco"
    }
    device_List.append(Router)
    
config_command = ['access-list 5 permit host 1.1.1.1','ntp server 192.167.1.1']

for each_device in device_List:
    connect = ConnectHandler(**each_device)
    connect.enable()
    output = connect.send_config_set(config_command)
    print(output)
    connect.disconnect()