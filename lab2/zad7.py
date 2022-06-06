import socket
import sys


if len(sys.argv) > 1:
    remote_server = sys.argv[1]
    remote_server_ip = socket.gethostbyname(remote_server)
    remote_port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((remote_server_ip, remote_port))
    if result == 0:
        print("Śmiga")
        try:
            print(f"Service name: {socket.getservbyport(remote_port, 'tcp')}")
        except OSError:
            print(f"Service not found")
    else:
        print("Nie śmiga")

    sock.close()
