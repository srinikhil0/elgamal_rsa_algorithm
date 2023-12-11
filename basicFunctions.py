# Function to check if a number is odd
def is_odd(value):
    """Determines if the given value is odd.

    Args:
        value (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return value % 2 != 0


# Euclidean algorithm to find the Greatest Common Divisor (GCD)
def gcd(a, b):
    """Computes the greatest common divisor of two numbers using the Euclidean algorithm.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: GCD of a and b.
    """
    if b == 0:
        return abs(a)
    return gcd(b, (a % b))


# Algorithm to find the multiplicative inverse
def multiplicative_inverse(x, modulo):
    """Finds the multiplicative inverse of x under modulo.

    Args:
        x (int): The number to find the inverse for.
        modulo (int): The modulo.

    Returns:
        int: The multiplicative inverse of x under modulo. Returns -1 if no inverse exists.
    """
    for y in range(1, modulo):
        if (x * y) % modulo == 1:
            return y
    return -1


# Basic Fast Exponentiation Algorithm
def basic_fast_exponent(base, exponent, modulo):
    """Computes base raised to the exponent modulo a number using a basic fast exponentiation approach.

    Args:
        base (int): The base number.
        exponent (int): The exponent.
        modulo (int): The modulo.

    Returns:
        int: Result of (base ** exponent) % modulo.
    """
    result = 1
    while exponent != 0:
        if exponent % 2 == 0:
            base = (base ** 2) % modulo
            exponent //= 2
        else:
            result = (base * result) % modulo
            exponent -= 1
    return result


# Improved Fast Exponentiation Algorithm
def improved_fast_exponent(base, exponent, modulo):
    """
    Computes base raised to the exponent modulo a number using an improved fast exponentiation approach.

    Args:
        base (int): The base number.
        exponent (int): The exponent.
        modulo (int): The modulo.

    Returns:
        int: Result of (base ** exponent) % modulo.
    """
    result = 1
    exponent = int(exponent)  # Ensure exponent is an integer
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulo
        base = (base ** 2) % modulo
        exponent >>= 1
    return result



# Extended Euclidean Algorithm
def extended_gcd(a, b):
    """Extended Euclidean algorithm to find integers x and y such that ax + by = gcd(a, b).

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        tuple: A tuple containing the GCD of a and b, and the coefficients x and y.
    """
    if a == 0:
        return b, 0, 1
    gcd_value, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_value, x, y
