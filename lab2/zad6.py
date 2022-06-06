import socket


remote_ip = '212.182.24.236'
remote_port = 2902
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    sock.send('12'.encode('utf-8'))
    sock.send("-".encode('utf-8'))
    sock.send("5".encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
else:
    print('Nie śmiga')

sock.close()
