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


def encode_text_msg_websocket(data):
    bytesFormatted = []
    bytesFormatted.append(chr(129))
    bytesRaw = data.encode()
    bytesLength = len(bytesRaw)
    if bytesLength <= 125:
        bytesFormatted.append(chr(bytesLength))
    elif 126 <= bytesLength <= 65535:
        bytesFormatted.append(chr(126))
        bytesFormatted.append((chr(bytesLength >> 8) & 255))
        bytesFormatted.append(chr(bytesLength & 255))
    else:
        bytesFormatted.append(chr(127))
        bytesFormatted.append(chr((bytesLength >> 56) & 255))
        bytesFormatted.append(chr((bytesLength >> 48) & 255))
        bytesFormatted.append(chr((bytesLength >> 40) & 255))
        bytesFormatted.append(chr((bytesLength >> 32) & 255))
        bytesFormatted.append(chr((bytesLength >> 24) & 255))
        bytesFormatted.append(chr((bytesLength >> 16) & 255))
        bytesFormatted.append(chr((bytesLength >> 8) & 255))
        bytesFormatted.append(chr(bytesLength & 255))
    send_str = ""
    for i in bytesFormatted:
        send_str += i

    send_str = send_str.encode()
    send_str += bytesRaw
    return send_str


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
