import socket

address = input("Adres IP:")
hostname = socket.gethostbyaddr(address)
print(hostname)
