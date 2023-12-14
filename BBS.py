# Blum-Blum-Shub Pseudorandom Number Generator

import basicFunctions
import random


def find_initial_value(num):
    """
    Finds an initial value that is relatively prime to 'num'.

    Args:
        num (int): A number to find a relative prime for.

    Returns:
        int: An initial value that is relatively prime to 'num'.
    """
    while True:
        initial_value = random.randint(1, num)
        if basicFunctions.gcd(initial_value, num) == 1:
            return initial_value


def get_bit(modulus):
    """
    Generates a single pseudorandom bit using the Blum-Blum-Shub algorithm.

    Args:
        modulus (int): The modulus used in the algorithm, typically p * q where p and q are prime numbers.

    Returns:
        int: A single pseudorandom bit.
    """
    initial_value = find_initial_value(modulus)
    s = initial_value
    iteration_count = 50  # Reduced number of iterations for efficiency
    for _ in range(iteration_count):
        s = pow(s, 2, modulus)  # More efficient squaring and modulo operation
    return s % 2



def generate_random_bits(count, p, q):
    """
    Generates a sequence of pseudorandom bits using the Blum-Blum-Shub algorithm.

    Args:
        count (int): The number of bits to generate.
        p (int): A prime number.
        q (int): Another prime number.

    Returns:
        str: A string of pseudorandom bits.
    """
    modulus = p * q
    return ''.join(str(get_bit(modulus)) for _ in range(count))


def random_number_generator():
    """
    Generates a random number using the Blum-Blum-Shub algorithm.

    Returns:
        int: A random number generated using the Blum-Blum-Shub algorithm.
    """
    bits = generate_random_bits(24, 11, 23)  # 24-bit number, p=11, q=23
    return int(bits, 2)


