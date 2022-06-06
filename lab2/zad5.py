import socket


remote_ip = '212.182.24.236'
remote_port = 2901
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    while True:
        message = input()
        sock.send(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
else:
    print('Nie śmiga')

sock.close()
