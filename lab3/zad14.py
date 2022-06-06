import socket


datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29".split()
source_port = int("".join(datagram[:2]), 16)
dest_port = int("".join(datagram[2:4]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[32:]])
print(source_port)
print(dest_port)
print(data)
odp = f"zad13odp;src;{source_port};dst;{dest_port};data;{data}"

# remote_ip = '212.182.24.236'
# remote_port = 2909
remote_ip = 'localhost'
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
