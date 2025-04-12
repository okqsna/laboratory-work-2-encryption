"""
Generation of secret and public keys 
with RSA algorithm
"""
import math
import secrets



# def find_prime(n: int) -> list:
#     """
#     Generating all prime numbers with Eratosthenes sieve

#     :param n: int, amount of numbers from which we generate prime numbers
#     :return: list, primes number
#     """
#     all_primes = [True] * n
#     all_primes[0], all_primes[1] = False, False

#     for i in range(2, math.isqrt(n)):
#         if all_primes[i]:
#             for j in range(i**2, n, i):
#                 all_primes[j] = False

#     return [i for i in range(n) if all_primes[i]]


def rsa_algorithm():
    """
    Algorithm for generation of keys

    :param num_1: int, amount of numbers from which we generate prime numbers
    """

    # generation of random prime numbers with 2048 bits
    number_one, number_two = secrets.randbits(2048), secrets.randbits(2048)

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

