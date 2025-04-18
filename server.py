"""
Server part of a messenger
"""
import socket
import threading
from rsa_algorithm import rsa_algorithm
from hashing import hash_message, check_message_integrity
from encryption import encrypt, decrypt

class Server:
    """
    Class object for server
    """

    def __init__(self, port: int) -> None:
        self.host = '127.0.0.1'
        self.port = port
        self.clients = []
        self.clients_keys = {}
        self.username_lookup = {}
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dct = rsa_algorithm()
        self.server_public_key_n = dct['n']
        self.secret_key = dct['secret_key_d']
        self.server_public_key_e = dct['euler_function']

    def start(self):
        """sending public keys to clients"""
        self.s.bind((self.host, self.port))
        self.s.listen(100)

        while True:
            c, _ = self.s.accept()
            username = c.recv(1024).decode()
            client_key = c.recv(2048).decode()
            client_public_n, client_public_e = eval(client_key)
            print(f"{username} tries to connect")
            self.clients.append(c)
            self.clients_keys[c] = (client_public_n, client_public_e)
            self.username_lookup[c] = username

            # Send server's public key to client
            c.send(str((self.server_public_key_n, self.server_public_key_e)).encode())

            threading.Thread(target=self.handle_client, args=(c,)).start()

    def handle_client(self, c):
        """receive message and decode"""
        while True:
            try:
                msg = c.recv(2048).decode()
                if msg:
                    print(f"[server]: Received message from {self.username_lookup[c]}: {msg}")
                    encr_str, received_hash = msg.split("/")
                    encr_blocks = list(map(int, encr_str.split(",")))
                    decrypted = decrypt(encr_blocks, self.secret_key, self.server_public_key_n)

                    if check_message_integrity(received_hash, decrypted):
                        print(f"[server]: Decrypted message: {decrypted}")
                        self.broadcast(decrypted, exclude=c)
                    else:
                        print("[warning]: integrity check failed on server")

            except Exception:
                print("[server]: Client disconnected")
                self.clients.remove(c)
                break

    def broadcast(self, msg: str, exclude=None):
        """send meccage and encode"""
        for client in self.clients:
            if client == exclude:
                continue
            try:
                public_n, public_e = self.clients_keys[client]
                encr_blocks = encrypt(msg, public_n, public_e)
                encr_str = ",".join(map(str, encr_blocks))
                hashed = hash_message(msg)
                msg_encr = encr_str + "/" + hashed
                print(f"[debug] Sending client {self.username_lookup[client]}: {msg_encr}")
                client.send(msg_encr.encode())
            except Exception as e:
                print(f"[server]: Failed to send message to {self.username_lookup.get(client, '?')}: {e}")

if __name__ == "__main__":
    s = Server(6000)
    s.start()
