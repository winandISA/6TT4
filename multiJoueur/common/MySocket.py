import json
import struct
import socket

class Mysocket:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send_msg(self, obj: dict) -> None:
        payload = json.dumps(obj).encode("utf-8")
        header = struct.pack("!I", len(payload))
        self.sock.sendall(header + payload)

    def recvall(self, n: int) -> bytes:
        data = b""
        while len(data) < n:
            chunk = self.sock.recv(n - len(data))
            if not chunk:
                return b""
            data += chunk
        return data

    def recv_msg(self) -> dict | None:
        header = self.recvall(4)
        if not header:
            return None
        size = struct.unpack("!I", header)[0]
        payload = self.recvall(size)
        if not payload:
            return None
        return json.loads(payload.decode("utf-8"))

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass
