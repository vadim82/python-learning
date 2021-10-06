import socket
import sys
from typing import Any, Dict


class Resolver:

    def __init__(self) -> None:
        self._cache: Dict[str, str] = dict()

    def __call__(self, host: str) -> Any:
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host: str) -> bool:
        return host in self._cache


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("First argument must be a host")

    host_name = sys.argv[1]
    host = Resolver()(host_name)
    print(host)
