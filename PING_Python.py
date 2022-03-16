import os # Biblioteca que integra recursos do S.O como o próprio "PING"
print("-" * 60)
ping_host = input("Informe o IP ou Host: ")
print("-" * 60)
os.system('ping -n 8 {}'.format(ping_host))
print("-" * 60)