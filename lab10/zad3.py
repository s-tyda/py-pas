#!/usr/bin/env python
import socket


def recv_all(sock):
    data = b""
    try:
        while b"\r\n\r\n" not in data:
            data += sock.recv(1024)
        return data
    except TimeoutError:
        return data


remote_ip = "echo.websocket.events"
remote_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex((remote_ip, remote_port))

handshake = "GET /chat HTTP/1.1\r\n" \
            "Host: echo.websocket.events\r\n" \
            "Upgrade: websocket\r\n" \
            "Connection: Upgrade\r\n" \
            "Sec-WebSocketProtocol: chat\r\n" \
            "Sec-WebSocket-Version: 13\r\n" \
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n\r\n"
sock.sendall(handshake.encode())
response = recv_all(sock)
print(response)

message = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
frame = bytearray()
frame.append(0x82)
frame.append(int('11111110', 2))
frame.append(0x00)
frame.append(0x81)
frame.append(0x00)
frame.append(0x00)
frame.append(0x00)
frame.append(0x00)
frame.append(0x00)
frame.append(0x00)
sock.sendall(frame)
sock.sendall(message.encode())


print("---ECHO RESPONSE---")
sock.settimeout(3)
response = recv_all(sock)
print(response)
