"""
Generation of secret and public keys 
with RSA algorithm
"""


import random
import math


def is_prime_num(n):
    """
    Checking if number is prime
    """
    if n == 0 or n == 1 or n < 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
    return True


def rsa_algorithm(num_1, num_2):
    """
    Algorithm for generation of keys
    """

    # generation of random prime numbers
    prime_numbers = [i for i in range(num_1, num_2) if is_prime_num(i)]
    print(prime_numbers)
    number_one, number_two = random.sample(prime_numbers, 2)

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

    return {'public_key': public_key_part_one, 'public_key_part_one': public_key_part_one,\
            'secret_key': d, 'euler function': euler_function}

# print(rsa_algorithm(10000, 30000))