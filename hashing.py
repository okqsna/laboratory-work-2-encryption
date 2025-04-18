"""hashing and message integrity"""
import hashlib

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

