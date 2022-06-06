import socket


datagram = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b " \
           "c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 " \
           "80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 " \
           "00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 " \
           "72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e".split()
first_byte = bin(int(datagram[0], 16))[2:-4]
protocol_version = int(first_byte, 2)
source_ip = ".".join([str(int(x, 16)) for x in datagram[12:16]])
dest_ip = ".".join([str(int(x, 16)) for x in datagram[16:20]])
protocol_type = 6
source_port = int("".join(datagram[20:22]), 16)
dest_port = int("".join(datagram[22:24]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[52:]])

odp1 = f"zad15odpA;ver;{protocol_version};srcip;{source_ip};dstip;{dest_ip};type;{protocol_type}"
odp2 = f"zad15odpB;srcport;{source_port};dstport;{dest_port};data;{data}"

print(odp1)
print(odp2)

# remote_ip = '212.182.24.236'
# remote_port = 2911
remote_ip = 'localhost'
remote_port = 2137
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    sock.settimeout(1)
    sock.send(odp1.encode('utf-8'))
    result = sock.recv(1024)
    print(result.decode())
    sock.send(odp2.encode('utf-8'))
    result = sock.recv(1024)
    print(result.decode())
else:
    print('Nie śmiga')

sock.close()