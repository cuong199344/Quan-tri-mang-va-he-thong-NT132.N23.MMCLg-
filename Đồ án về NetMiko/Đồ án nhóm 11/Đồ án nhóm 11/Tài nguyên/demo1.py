from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.130",
    "username": "admin",
    "password": "netmiko",
    "secret": "cisco",
}

connect = ConnectHandler(**R1)

print('ket noi thanh cong\n')
connect.enable()
# int = ["int e0/1","ip add 192.168.1.129 255.255.255.0","exit"]

# print(connect.send_config_set(int))
# print(connect.send_command('sh ip int br'))

dict_int = {
    "e0/1": "192.169.1.120 255.255.255.0",
    "e0/2": "192.170.1.119 255.255.255.0",
    "e0/3": "192.171.1.118 255.255.255.0"
}

for i in dict_int:
    config = ["int "+i,"no shutdown","ip add "+dict_int[i],"exit"]
    print(connect.send_config_set(config))
    
print(connect.send_command('sh ip int br'))