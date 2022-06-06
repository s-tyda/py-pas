from typing import Callable, TypeVar, Any
import functools
import time
import socket

T = TypeVar('T')


def timeit(method: Callable[..., T]) -> Callable:
    @functools.wraps(method)
    def timed(*args: Any, **kwargs: Any) -> T:
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        if args and isinstance(args[0], object):
            print(f"{args[0].__class__.__name__}::{method.__name__} execution time: {(end - start) * 1000}ms")
        else:
            print(f"{method.__name__} execution time: {(end - start) * 1000}ms")
        return result

    return timed

@timeit
def better_test(result_stream, sock):
    if result_stream == 0:
        print("Śmiga")
        sock.settimeout(1)
        sock.send("sdhhvskjvbhjdsbhjhj".encode('utf-8'))
        result = sock.recv(1024)
        print(result.decode())
    else:
        print('Nie śmiga')


def test_udp():
    remote_ip = '212.182.24.236'
    remote_port = 2901
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result_stream = sock.connect_ex((remote_ip, remote_port))

    better_test(result_stream, sock)

    sock.close()


def test_tcp():
    remote_ip = '212.182.24.236'
    remote_port = 2900
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_stream = sock.connect_ex((remote_ip, remote_port))

    better_test(result_stream, sock)

    sock.close()



print("TCP")
test_tcp()
print("UDP")
test_udp()

