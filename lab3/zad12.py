import socket


remote_ip = '212.182.24.236'
remote_port = 2908
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    message = input()
    message = message.ljust((len(message)//20 + 1) * 20)
    result = b""
    sock.settimeout(1)
    sock.sendall(message.encode('utf-8'))
    try:
        while True:
            data = sock.recv(20)
    except socket.timeout:
        result = result.decode('utf-8').strip()
        print(result)
else:
    print('Nie śmiga')

sock.close()
