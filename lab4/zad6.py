import socket

PORT = 2137
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    try:
        while True:
            data, address = sock.recvfrom(1024)
            data = data.decode("utf-8")
            print(data)
            if data:
                sock.sendto((str(socket.gethostbyname(data)).encode("utf-8")), address)
                break
    except:
        pass
    finally:
        sock.close()
