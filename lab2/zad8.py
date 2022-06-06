import sys
import socket

try:
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Zła licza argsów")
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        print(result)
        if result == 0:
            print(f"Port {port} otwarty")
        try:
            print(f"Service name: {socket.getservbyport(port, 'tcp')}")
        except OSError:
            print(f"Service not found")

        sock.close()
except socket.gaierror:
    print("Zły hostname")
except socket.error:
    print("Coś nie dziaa!")
