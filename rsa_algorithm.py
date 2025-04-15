"""
Generation of secret and public keys 
with RSA algorithm
"""
import math
from secrets import randbits
from sympy import nextprime

def rsa_algorithm():
    """
    Algorithm for generation of keys

    :param num_1: int, amount of numbers from which we generate prime numbers
    """

    # generation of random prime numbers with 1024 bits
    number_one, number_two = nextprime(randbits(1024)), nextprime(randbits(1024))

    # RSA algorithm start
    public_key_part_one = number_one * number_two
    euler_function = (number_one - 1) * (number_two - 1)

    # Finding small number whose gcd with euler function is 1
    e = None
    for i in range(2, 200):
        if math.gcd(euler_function, i) == 1:
            e = i
            break

    # secret key generation
    d = pow(e, -1, euler_function)

    return {'public_key': public_key_part_one, 'n': public_key_part_one,\
            'secret_key_d': d, 'euler function': euler_function}
print(rsa_algorithm())