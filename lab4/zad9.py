import socket

PORT = 2137
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    try:
        data, address = sock.recvfrom(1024)
        try:
            data = data.decode("utf-8").split(";")
            if data[0] != "zad14odp" or data[1] != "src" or data [3] != "dst" or data[5] != "data":
                raise ValueError
            if data[2] == "60788" and data[4] == "2901" and data[6] == "programming in python is fun":
                sock.sendto("TAK".encode("utf-8"), address)
            else:
                sock.sendto("NIE".encode("utf-8"), address)
        except:
            sock.sendto("BAD SYNTAX".encode("utf-8"), address)
    except:
        break
    finally:
        sock.close()
