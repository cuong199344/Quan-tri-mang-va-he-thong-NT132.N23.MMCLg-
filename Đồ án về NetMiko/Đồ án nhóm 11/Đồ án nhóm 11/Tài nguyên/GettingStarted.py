from netmiko import ConnectHandler
import os

R1 = {
    'device_type': 'cisco_ios',
    'ip' : '192.168.1.130',
    'username' : 'admin',
    'password' : 'netmiko',
    'secret' : 'cisco',
}

connect = ConnectHandler(**R1)

print('Ket noi thanh cong\n')
connect.enable()
# print(connect.find_prompt())

# int = ["int e0/1","no shut", "ip add 192.168.1.128 255.255.255.0","exit"]
# print(connect.send_config_set(int))
# print(connect.send_command('sh ip int br'))
# dict_int = {
#     "e0/1": "192.169.1.150 255.255.255.0",
#     "e0/2": "192.170.1.151 255.255.255.0",
#     "e0/3": "192.171.1.152 255.255.255.0",
# }
# for i in dict_int:
#     config = ["int "+i,"no shut","ip add "+dict_int[i],"exit"]
#     print(connect.send_config_set(config))

print(connect.send_command('sh ip int br'))

output = connect.send_command('sh ip int br')

path = os.getcwd()
filename = 'int_down.txt'
int_status = 'down'
count = 0

for line in output.splitlines():
    if "Interface" in line:
        continue
    elif int_status in line:
        with open(filename, 'a') as f:
            f.write(line)
            count += 1
print('So interface down cua thiet bi:\t',count)
print('Thong tin duoc luu tai {} theo duogn dan {}.'.format(filename, path))  


