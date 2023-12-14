import unittest
import math
import basicFunctions

# Including the provided Baby-step Giant-step algorithm code directly here for testing purposes
def baby_step_giant_step(base, element, modulus):
    step_size = math.ceil(math.sqrt(modulus - 1))
    baby_steps = {pow(base, j, modulus): j for j in range(step_size)}
    base_step = pow(base, step_size, modulus)
    inverse_base_step = basicFunctions.multiplicative_inverse(base_step, modulus)

    current = element
    for i in range(step_size):
        if current in baby_steps:
            return i * step_size + baby_steps[current]
        current = (current * inverse_base_step) % modulus

    return -1

# Unit tests for Baby-step Giant-step algorithm
class TestBabyStepGiantStep(unittest.TestCase):

    def test_small_numbers(self):
        """Test the algorithm with small numbers."""
        base = 2
        modulus = 1019  # A prime number
        exponent = 10  # Known exponent
        element = pow(base, exponent, modulus)
        result = baby_step_giant_step(base, element, modulus)
        self.assertEqual(result, exponent, "Discrete logarithm of element to the base should be the known exponent")

    def test_large_numbers(self):
        """Test the algorithm with larger numbers."""
        base = 2
        modulus = 100003  # A larger prime number
        exponent = 20000  # Known exponent
        element = pow(base, exponent, modulus)
        result = baby_step_giant_step(base, element, modulus)
        self.assertEqual(result, exponent, "Discrete logarithm of element to the base should be the known exponent")

if __name__ == '__main__':
    unittest.main()

