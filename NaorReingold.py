# Naor-Reingold Pseudorandom Number Generator

import random, basicFunctions

def generate_a(n, pq, x):
    """
    Generates a pseudorandom number based on the Naor-Reingold construction.

    Args:
        n (int): The length of the array.
        pq (int): The product of two prime numbers.
        x (int): An input value to the pseudorandom generator.

    Returns:
        int: A pseudorandom number.
    """
    arr0 = [random.randint(1, pq) for _ in range(n)]
    arr1 = [random.randint(1, pq) for _ in range(n)]
    arr = [arr1[i] if bit == '1' else arr0[i] for i, bit in enumerate(bin(x)[2:].zfill(n))]
    arr_sum = sum(arr)
    return basicFunctions.improved_fast_exponent(arr_sum, pq, find_square(pq))


def find_square(num):
    """
    Finds a square value in a specific range.

    Args:
        num (int): The range limit.

    Returns:
        int: A square value within the given range.
    """
    while True:
        sqrt_candidate = random.randint(1, num)
        if basicFunctions.gcd(sqrt_candidate, num) == 1:
            return (sqrt_candidate ** 2) % num


def generate_b(n):
    """
    Generates a random binary string of length 2n.

    Args:
        n (int): The length of the half of the binary string.

    Returns:
        str: A random binary string of length 2n.
    """
    return ''.join(str(random.randint(0, 1)) for _ in range(2 * n))


def get_bit(n, p, q, x):
    """
    Computes a single pseudorandom bit.

    Args:
        n (int): A fixed number.
        p (int): A prime number.
        q (int): Another prime number.
        x (int): An input value to the pseudorandom generator.

    Returns:
        int: A single pseudorandom bit.
    """
    num = generate_a(n, p * q, x)
    binary_a = bin(num)[2:].zfill(2 * n)
    binary_b = generate_b(n)
    result = int(binary_a[-1]) * int(binary_b[-1])
    return result


def get_random_bits(count):
    """
    Generates a random bit string of a given length.

    Args:
        count (int): The length of the bit string.

    Returns:
        str: A random bit string.
    """
    return ''.join(str(get_bit(6, 47, 37, 43)) for _ in range(count))


def random_number_generator():
    """
    Generates a random number from a bit string.

    Returns:
        int: A random number.
    """
    bits = get_random_bits(24)
    return int(bits, 2)


def random_bit_string_generator():
    """
    Generates a random bit string.

    Returns:
        str: A random bit string.
    """
    return get_random_bits(24)



# generating x-bits long number
# n is a fixed number, x is a given number
# both p & q are prime numbers
# In this example, n = 6, p = 37, q = 47, x = 43
# print(RandGen())



