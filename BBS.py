# Blum-Blum-Shub Pseudorandom Number Generator

import random, basicFunctions

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
    bits = []
    for _ in range(modulus):
        s = (s ** 2) % modulus
        bits.append(s % 2)
    return bits[-1]


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


# generating 24-bit long number
# both p & q are prime numbers that also ≡ 3%4
# In this example, p = 11, q = 23
# print(RandGen())
