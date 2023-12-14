# Miller-Rabin Primality Test

import random, basicFunctions, BBS, NaorReingold

def miller_rabin_test(number):
    """
    Performs the Miller-Rabin primality test on a given number.

    Args:
        number (int): The number to test for primality.

    Returns:
        bool: True if the number is likely prime, False otherwise.
    """
    exponent = 0
    odd_component = number - 1
    while not basicFunctions.is_odd(odd_component):  # Decompose (number - 1) into 2^exponent * odd_component
        odd_component /= 2
        exponent += 1
    base = random.randint(1, number - 1)
    for i in range(exponent):
        if i == 0:
            result = basicFunctions.improved_fast_exponent(base, odd_component, number)
            if result in (1, -1 % number):
                return True
        else:
            result = basicFunctions.improved_fast_exponent(base, (2 ** i) * odd_component, number)
            if result == (-1 % number):
                return True
    return False


def generate_primes(count, method):
    """
    Generates a list of prime numbers using different random number generation methods.

    Args:
        count (int): The number of primes to generate.
        method (int): The random number generation method to use (0, 1, or 2).

    Returns:
        list: A list of prime numbers.
    """
    primes = []
    while count > 0:
        if method == 0:
            num = random.randint(1000, 10000)
        elif method == 1:
            num = NaorReingold.random_number_generator()
        elif method == 2:
            num = BBS.random_number_generator()
        else:
            return primes
        if not basicFunctions.is_odd(num):
            num += 1
        if miller_rabin_test(num) and miller_rabin_test(num) and miller_rabin_test(num):
            primes.append(num)
            count -= 1
    return primes


def generate_modulus(count, method):
    """
    Generates a modulus from two prime numbers.

    Args:
        count (int): The number of prime numbers to generate.
        method (int): The random number generation method to use.

    Returns:
        tuple: A tuple containing the modulus and the two prime numbers.
    """
    primes = generate_primes(count, method)
    return primes[0] * primes[1], primes[0], primes[1]

