import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

for ip in dump:
    print("-" * 60)
    print("Verificando o IP: ",ip)
    print("-" * 60)
    os.system('ping -n 1 {}'.format(ip))
    time.sleep(2)