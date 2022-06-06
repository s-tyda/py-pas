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
            if data[0] != "zad15odpA" or data[1] != "ver" or data[3] != "srcip" or data[5] != "dstip" or data[7] != "type":
                raise ValueError
            if data[2] == "4" and data[4] == "212.182.24.27" and data[6] == "192.168.0.2" and data[8 == "6"]:
                sock.sendto("TAK".encode("utf-8"), address)
            else:
                sock.sendto("NIE".encode("utf-8"), address)
        except:
            sock.sendto("BAD SYNTAX".encode("utf-8"), address)

        data, address = sock.recvfrom(1024)
        try:
            data = data.decode("utf-8").split(";")
            if data[0] != "zad15odpB" or data[1] != "srcport" or data[3] != "dstport" or data[5] != "data":
                raise ValueError
            if data[2] == "2900" and data[4] == "47526" and data[6] == "network programming is fun":
                sock.sendto("TAK".encode("utf-8"), address)
            else:
                sock.sendto("NIE".encode("utf-8"), address)
        except:
            sock.sendto("BAD SYNTAX".encode("utf-8"), address)
    except:
        break
    finally:
        sock.close()
