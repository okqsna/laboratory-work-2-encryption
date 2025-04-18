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
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def start(self):
        self.s.bind((self.host, self.port))
        self.s.listen(100)

        # generate keys ...
        rsa = rsa_algorithm()
        public_key = rsa['n']
        secret_key = rsa['secret_key_d']
        euler_func = rsa['euler_function']

        while True:
            c, addr = self.s.accept()
            username = c.recv(1024).decode()
            client_key = c.recv(2048).decode()
            print(f"{username} tries to connect")
            self.broadcast(f'new person has joined: {username}')
            self.username_lookup[c] = username
            self.clients.append(c)
            print(f"connected with {addr}")

            # send public key to the client
            c.send(str(public_key).encode())
            # ...

            # encrypt the secret with the clients public key

            # ...

            # send the encrypted secret to a client

            # ...

            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def broadcast(self, msg: str):
        for client in self.clients:

            # encrypt the message

            # ...

            client.send(msg.encode())

    def handle_client(self, c: socket, addr): 
        while True:
            msg = c.recv(1024)

            for client in self.clients:
                if client != c:
                    client.send(msg)

if __name__ == "__main__":
    s = Server(6000)
    s.start()
