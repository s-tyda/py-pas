import socket


remote_ip = '212.182.24.236'
remote_port = 2907
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.settimeout(0.5)
result = sock.connect_ex((remote_ip, remote_port))
if result == 0:
    print("Śmiga")
    message = input("Podaj hostname byku\n")
    sock.send(message.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
else:
    print('Nie śmiga')
    
sock.close()
