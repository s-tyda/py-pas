import socket


remote_ip = socket.gethostbyname('ntp.task.gda.pl')
remote_port = 13

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    data = sock.recv(1024)
    print(data.decode('utf-8'))
else:
    print('Nie śmiga')

sock.close()
