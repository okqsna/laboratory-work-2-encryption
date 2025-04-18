"""
Hashing and message integrity
"""
import hashlib

def hash_message(word: str):
    """
    Computes the SHA3-512 hash of the input message.

    :param word: str, message 
    """
    return hashlib.sha3_512(word.encode('utf-8')).hexdigest()


def check_message_integrity(received_hash, decrypted: str):
    """
    Checks whether the received message has maintained its integrity.
    :param received_hash: hash received from user's message
    :param decrypted: str, decrypted message to check hash for
    """
    calculated_hash = hash_message(decrypted)
    return calculated_hash == received_hash
