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
    size = modulus - 1
    step_size = math.ceil(math.sqrt(size))

    # Initialize arrays for the baby steps and giant steps
    baby_steps = [-1] * step_size
    giant_steps = [-1] * step_size

    # Calculate baby steps
    for j in range(step_size):
        baby_steps[j] = pow(element, j, modulus)

    # Calculate multiplicative inverse and prepare for giant steps
    inverse_element = basicFunctions.multiplicative_inverse(element, modulus)
    multiplier = pow(inverse_element, step_size, modulus)

    # Calculate giant steps
    for i in range(step_size):
        giant_steps[i] = (base * pow(multiplier, i, modulus)) % modulus

    # Search for matching elements in baby steps and giant steps
    for k in range(step_size):
        for h in range(step_size):
            if baby_steps[k] == giant_steps[h]:
                return h * step_size + k

    return -1


# Example usage
# result = baby_step_giant_step(3305, 1785, 21773)
# print(result)
