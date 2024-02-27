from netmiko import ConnectHandler
import json

R1 = {
    'device_type': 'cisco_ios',
    'ip' : '192.168.1.62',
    'username' : 'admin',
    'password' : 'netmiko',
    'secret' : 'cisco',
}
connect = ConnectHandler(**R1)

print('Connecting')
connect.enable()
output = connect.send_command('sh ip int br', use_textfsm=True)
not_connect_interfaces = [item['intf'] for item in output if item['status'] == 'administratively down' ]

for interface in not_connect_interfaces:
    commands = [f"interface {interface}", 'no shutdown']
    config_output = connect.send_config_set(commands)
    print(config_output)

print(connect.send_command('sh ip int br'))