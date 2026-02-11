import socket
import threading
import time
import json
import struct

from multiJoueur.common.MySocket import Mysocket

HOST = "0.0.0.0"
PORT = 5000
TICK_RATE = 30  # envois STATE par seconde

sock =
# ----- Etat du jeu -----

lock = threading.Lock()
clients: list[tuple[socket.socket, str]] = []  # (conn, color)

positions = {
    "RED":  [100, 150],
    "BLUE": [300, 150],
}

def broadcast_state() -> None:
    with lock:
        state = {
            "type": "state",
            "players": {
                "RED": positions["RED"],
                "BLUE": positions["BLUE"],
            }
        }
        conns = [c for c, _ in clients]

    dead = []
    for c in conns:
        try:
            send_msg(c, state)
        except OSError:
            dead.append(c)

    if dead:
        with lock:
            clients[:] = [(c, col) for (c, col) in clients if c not in dead]

def client_loop(conn: socket.socket, color: str) -> None:
    try:
        while True:
            msg = recv_msg(conn)
            if msg is None:
                return

            if msg.get("type") == "move":
                dx = int(msg.get("dx", 0))
                dy = int(msg.get("dy", 0))
                with lock:
                    positions[color][0] += dx
                    positions[color][1] += dy

    finally:
        with lock:
            for i, (c, col) in enumerate(clients):
                if c is conn:
                    clients.pop(i)
                    break
        try:
            conn.close()
        except OSError:
            pass

def game_loop() -> None:
    dt = 1.0 / TICK_RATE
    while True:
        broadcast_state()
        time.sleep(dt)

def main():
    with Mysocket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(2)

        print(f"Serveur sur {HOST}:{PORT} (attente de 2 joueurs)")

        # Accepter 2 clients, attribuer couleur
        colors = ["RED", "BLUE"]
        while True:
            conn, addr = server.accept()
            with lock:
                if len(clients) >= 2:
                    # serveur limité à 2 pour cette démo
                    try:
                        send_msg(conn, {"type": "error", "message": "Server full"})
                    except OSError:
                        pass
                    conn.close()
                    continue

                color = colors[len(clients)]
                clients.append((conn, color))

            print(f"Client {addr} connecté -> {color}")
            send_msg(conn, {"type": "welcome", "color": color})

            threading.Thread(target=client_loop, args=(conn, color), daemon=True).start()

            # Démarrer la boucle de jeu dès que le premier arrive (ok),
            # mais on peut aussi attendre 2 joueurs si tu préfères.
            if len(clients) == 1:
                threading.Thread(target=game_loop, daemon=True).start()

if __name__ == "__main__":
    main()
