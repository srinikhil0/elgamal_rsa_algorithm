# Baby-step Giant-step Algorithm

import math
import basicFunctions

def baby_step_giant_step(base, element, modulus):
    """
    Implements the Baby-step Giant-step algorithm to solve discrete logarithm problems.

    Args:
        base (int): The base of the logarithm.
        element (int): The element whose logarithm is to be calculated.
        modulus (int): The modulus for the logarithm operation.

    Returns:
        int: The discrete logarithm of the element to the given base under the specified modulus.
    """
    # Calculate the size of the steps
    step_size = math.ceil(math.sqrt(modulus - 1))

   # Calculate baby steps and store in a dictionary for efficient lookup
    baby_steps = {pow(base, j, modulus): j for j in range(step_size)}

    # Calculate multiplicative inverse of base^step_size for giant steps
    base_step = pow(base, step_size, modulus)
    inverse_base_step = basicFunctions.multiplicative_inverse(base_step, modulus)

    # Calculate and search for giant steps
    current = element
    for i in range(step_size):
        if current in baby_steps:
            return i * step_size + baby_steps[current]
        current = (current * inverse_base_step) % modulus

    return -1
