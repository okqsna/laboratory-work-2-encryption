"""
Client part of a messenger
"""

import socket
import threading
import time
from rsa_algorithm import rsa_algorithm
from encryption import encrypt, decrypt
from hashing import hash_message, check_message_integrity

class Client:
    """
    Class object for client
    """
    def __init__(self, server_ip: str, port: int, username: str) -> None:
        """
        Function initializes the body of a client.

        :param server_ip: str, ip of a server
        :param port: int, port to listen the server on
        :param username: str, name of a client to use
        """
        self.server_ip = server_ip
        self.port = port
        self.username = username
        rsa = rsa_algorithm()
        self.public_key_n = rsa['n']
        self.secret_key = rsa['secret_key_d']
        self.public_key_e = rsa['euler_function']
        self.server_public_n = None
        self.server_public_e = None

    @property
    def s(self):
        """
        Function returns connection with socket
        """
        return self.s

    @s.setter
    def s(self, value):
        """
        Function sets connection with socket
        """
        self.s = value

    def init_connection(self):
        """
        Function connects client with server
        """
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server_ip, self.port))
        except Exception as e:
            print("[client]: could not connect to server: ", e)
            return

        self.s.send(self.username.encode())
        time.sleep(0.1)
        # Send public key to server
        self.s.send(str((self.public_key_n, self.public_key_e)).encode())

        # Receive server's public key
        server_key = self.s.recv(2048).decode()
        decoded_server_key = server_key[1:-1].split(',')
        self.server_public_n = int(decoded_server_key[0].strip())
        self.server_public_e = int(decoded_server_key[0].strip())

        threading.Thread(target=self.read_handler).start()
        threading.Thread(target=self.write_handler).start()

    def read_handler(self):
        """
        Function helps client to 
        receive message and decode it.
        """
        while True:
            try:
                message = self.s.recv(2048).decode()
                print("[debug] Got message:", message)
                encr_str, received_hash = message.split("/")
                encr_blocks = list(map(int, encr_str.split(",")))
                decrypted = decrypt(encr_blocks, self.secret_key, self.public_key_n)
                if check_message_integrity(received_hash, decrypted):
                    print(f"[server]: {decrypted}")
                else:
                    print("[warning]: Message integrity check failed!")
            except Exception as e:
                print("[error]: Failed to decode or decrypt message:", e)
                break

    def write_handler(self):
        """
        Function helps to send message and encode them.
        """
        while True:
            message = input()
            if not message.isspace():
                hashed = hash_message(message)
                encr_blocks = encrypt(message, self.server_public_n, self.server_public_e)
                encr_str = ",".join(map(str, encr_blocks))
                payload = encr_str + "/" + hashed
                print(f'[encrypted message] {payload}')
                self.s.send(payload.encode())
            else:
                print('Message should contain at least 1 word)')
                break

if __name__ == "__main__":
    cl = Client("127.0.0.1", 6000, "b_g")
    cl.init_connection()
