import socket
import sys


if len(sys.argv) > 1:
    remote_server = sys.argv[1]
    remote_server_ip = socket.gethostbyname(remote_server)
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((remote_server_ip, port))
    if result == 0:
        print("Git")
    else:
        print("Niegit")
