import socket


datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e".split()
source_port = int("".join(datagram[:2]), 16)
dest_port = int("".join(datagram[2:4]), 16)
length = int("".join(datagram[4:6]), 16)
checksum = int("".join(datagram[6:8]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[8:]])
print(source_port)
print(dest_port)
print(length)
print(checksum)
print(data)
odp = f"zad14odp;src;{source_port};dst;{dest_port};data;{data}"

# remote_ip = '212.182.24.236'
remote_ip = 'localhost'
# remote_port = 2910
remote_port = 2137
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = sock.connect_ex((remote_ip, remote_port))

if result_stream == 0:
    print("Śmiga")
    sock.settimeout(1)
    sock.send(odp.encode('utf-8'))
    result = sock.recv(1024)
    print(result.decode())
else:
    print('Nie śmiga')

sock.close()
