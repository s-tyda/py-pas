import socket
from datetime import datetime

PORT = 2137
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1000)

while True:
    connection, address = sock.accept()
    try:
        while True:
            data = connection.recv(1024).decode("utf-8")
            print(data)
            if data:
                connection.sendall((str(datetime.utcnow()).encode("utf-8")))
                break
    except:
        pass
    finally:
        connection.close()
