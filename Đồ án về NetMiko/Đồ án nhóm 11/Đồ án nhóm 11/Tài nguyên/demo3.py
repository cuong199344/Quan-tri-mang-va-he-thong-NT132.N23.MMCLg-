from netmiko import ConnectHandler
import json

R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.62",
    "username": "admin",
    "password": "netmiko",
    "secret": "cisco"
}

connect = ConnectHandler(**R1)
connect.enable()
output = connect.send_command('sh ip int br',use_textfsm=True)
not_connected_int = [item['intf'] for item in output if item['status'] == 'administratively down']

for intf in not_connected_int:
    command = [f"interface {intf}", "no shutdown"]
    config_output = connect.send_config_set(command)
    print(config_output)
    
print(connect.send_command('sh ip int br'))