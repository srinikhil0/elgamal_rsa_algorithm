# Pollard’s Rho Factorization Algorithm

import basicFunctions, MRprimalityTest, random

def is_prime(number):
    """
    Checks if a number is prime using the Miller-Rabin primality test.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    return MRprimalityTest.miller_rabin_test(number)


def pollards_rho_factorization(number):
    """
    Pollard's Rho algorithm for integer factorization.

    Args:
        number (int): The number to factorize.

    Returns:
        int: A non-trivial factor of the number, or -1 if the algorithm needs to be reinitialized.
    """
    x, y = 2, (2**2) + 1
    for _ in range(number):
        gcd_value = basicFunctions.gcd(abs(x - y), number)
        if gcd_value != 1:
            return gcd_value
        elif gcd_value == number:
            print("The algorithm needs to be reinitialized.")
            return -1
        x = (x**2 + 1) % number
        y = ((y**2 + 1)**2 + 1) % number


def find_factors(number):
    """
    Finds two factors of a number using Pollard’s Rho algorithm.

    Args:
        number (int): The number to factorize.

    Returns:
        tuple: A tuple of two factors of the number.
    """
    factor = pollards_rho_factorization(number)
    if factor == -1:
        return -1, -1
    return factor, number // factor


def find_root_factor(number):
    """
    Finds a root factor of a number.

    Args:
        number (int): The number to find a root factor for.

    Returns:
        int: A root factor of the number.
    """
    if number in [1, 2, 5]:
        return number
    return pollards_rho_factorization(number)


def find_all_prime_factors(number):
    """
    Finds all prime factors of a number.

    Args:
        number (int): The number to find prime factors for.

    Returns:
        list: A list of all prime factors of the number.
    """
    factors = [0] * 10
    for i in range(10):
        if is_prime(number):
            factors[i] = number
            break
        else:
            root_factor = find_root_factor(number)
            number //= root_factor
            factors[i] = root_factor
    return factors


def primitive_root_search(prime):
    """
    Searches for a primitive root modulo a given prime number.

    Args:
        prime (int): The prime number to find a primitive root for.

    Returns:
        int: A primitive root modulo the prime number, or -1 if not found.
    """
    factors = find_all_prime_factors(prime - 1)
    for _ in range(10):
        candidate = random.randint(2, prime - 1)
        if all(basicFunctions.improved_fast_exponent(candidate, (prime - 1) // factor, prime) != 1 for factor in factors if factor != 0):
            return candidate
    return -1


def check_primitive_root(root, prime):
    """
    Checks if a number is a primitive root modulo a given prime.

    Args:
        root (int): The number to check.
        prime (int): The prime number.

    Returns:
        bool: True if the number is a primitive root modulo the prime, False otherwise.
    """
    factors = find_all_prime_factors(prime - 1)
    return all(basicFunctions.improved_fast_exponent(root, (prime - 1) // factor, prime) != 1 for factor in factors if factor != 0)


