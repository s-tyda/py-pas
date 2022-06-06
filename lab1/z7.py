import sys
import socket

try:
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Zła licza argsów")
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} otwarty")
        s.close()
except socket.gaierror:
    print("Zły hostname")
except socket.error:
    print("Coś nie dziaa!")
