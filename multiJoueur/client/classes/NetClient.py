# ----- Client réseau -----
import threading

from multiJoueur.common.MySocket import Mysocket


class NetClient:
    def __init__(self, host: str, port: int):
        self.sock = Mysocket(host, port)

        self.color = "?"
        self.players = {"RED": [100, 150], "BLUE": [300, 150]}
        self.lock = threading.Lock()

        welcome = self.sock.recv_msg()
        if welcome and welcome.get("type") == "welcome":
            self.color = welcome.get("color", "?")

        self.running = True
        threading.Thread(target=self._recv_loop, daemon=True).start()

    def _recv_loop(self):
        while self.running:
            msg = self.sock.recv_msg()
            if msg is None:
                self.running = False
                return

            if msg.get("type") == "state":
                players = msg.get("players", {})
                with self.lock:
                    if "RED" in players:
                        self.players["RED"] = players["RED"]
                    if "BLUE" in players:
                        self.players["BLUE"] = players["BLUE"]

    def move(self, dx: int, dy: int) -> None:
        self.sock.send_msg({"type": "move", "dx": dx, "dy": dy})

    def get_players(self):
        with self.lock:
            return {
                "RED": self.players["RED"][:],
                "BLUE": self.players["BLUE"][:]
            }

    def close(self):
        self.running = False
        self.sock.close()
