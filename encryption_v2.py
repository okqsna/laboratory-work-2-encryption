"""
Another version of encryption to be fixed
"""

def encryption(word, n, e):
    """
    Encrypting the message

    :param word: str, words to encrypt
    :param n: int, public key
    :param e: int, e from rsa
    """
    code = ''
    for i in word:
        s = str(ord(i)).zfill(4)
        code += s

    block_length = max_block_length(n)
    blocks = [int(code[i:i+block_length]) for i in range(0, len(code), block_length)]
    for i, _ in enumerate(blocks):
        blocks[i] = pow(blocks[i], e, n)

    return blocks

def decrypt(blocks, d, n):
    """
    Decrypting the message

    :param blocks: list, encrypted message
    :param d: int, private key
    :param n: int, public key
    """
    lst = ''
    result = ''
    for block in blocks:
        m = pow(block, d, n)
        lst += str(m).zfill(4)

    for i in range(0, len(lst), 4):
        result += chr(int(lst[i:i+4]))
    return result

def max_block_length(n):
    """
    Finding the max length of a block
    """
    k = 1
    while 10 ** k < n:
        k += 1
    return k


n_p, secret_key, euler = 3551, 1817, 17
block_decr = encryption('hello world', n_p, euler)
res = decrypt(block_decr, secret_key, n_p)
print(res)