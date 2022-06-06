import socket


remote_ip = '212.182.24.236'
remote_port = 2908
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    message = input()
    if len(message) < 20:
        message = message.ljust(20)
    chunks = [message[i:i+20] for i in range(0, len(message), 20)]
    result = ""
    for chunk in chunks:
        sock.send(message.encode('utf-8'))
        data = sock.recv(20)
        result += data.decode('utf-8')
    print(result)
else:
    print('Nie śmiga')

sock.close()
