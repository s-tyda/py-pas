import socket

# remote_ip = '212.182.24.236'
remote_ip = 'localhost'
remote_port = 2912
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    message = input()
    sock.send(message.encode('utf-8'))
    data = sock.recv(20)
    print(data.decode('utf-8'))
else:
    print('Nie śmiga')

sock.close()
