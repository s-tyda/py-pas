import socket


def recv_all(sock):
    data = b""
    while b"\r\n\r\n" not in data:
        data = data + sock.recv(1024)
    return data


def recv_until(sock, size):
    data = b""
    while len(data) < size:
        data = data + sock.recv(1)
    return data


remote_ip = 'httpbin.org'
remote_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex((remote_ip, remote_port))

request = 'POST /post HTTP/1.1\r\n' \
          'Host: httpbin.org\r\n' \
          'Content-Length: 114\r\n' \
          'Content-Type: application/x-www-form-urlencoded\r\n\r\n' \
          'custname=fsdf&custtel=sdfsdf&custemail=sdfsdf%40gmail.com&size=small&topping=bacon&delivery=12%3A15&comments=fgdfg\r\n\r\n'


sock.sendall(request.encode())

response = recv_all(sock)
headers = response.split(b'\r\n')

size = [int(header.split(b" ")[-1]) for header in headers if b"Content-Length:" in header][0]

data = recv_until(sock, size)

with open("zad9_4.html", "wb") as file:
    file.write(data)
