import socket

hostname = input("Hostname:")
ip = socket.gethostbyname(hostname)
print(ip)
