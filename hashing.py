"""hashing and message integrity"""
import hashlib
# from encryption_v2 import encryption, decrypt

def hash_message(word):
    """
    Computes the SHA3-512 hash of the input message.
    """
    return hashlib.sha3_512(word.encode('utf-8')).hexdigest()


def check_message_integrity(received_hash, decrypted):
    """
    Checks whether the received message has maintained its integrity.
    """
    calculated_hash = hash_message(decrypted)
    return calculated_hash == received_hash

# n_p, secret_key, euler = 3551, 1817, 17
# MES = 'hello world'
# encr = encryption(MES, n_p, euler)
# decr = decrypt(encr, secret_key, n_p)

# HASHED = hash_message(MES)
# print(HASHED)

# print(check_message_integrity(HASHED, decr))
