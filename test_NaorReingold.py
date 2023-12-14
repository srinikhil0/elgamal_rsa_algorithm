import unittest
import basicFunctions
import NaorReingold 

class TestNaorReingoldPseudorandomNumberGenerator(unittest.TestCase):

    def test_random_number_generator_large_numbers(self):
        """Test if the random number generator produces an integer with larger parameters."""
        # Adjust these values to larger primes and a larger fixed number n
        n = 10
        p = 100003  # A larger prime number
        q = 100019  # Another larger prime number
        x = 50000   # A larger input value
        num = NaorReingold.generate_a(n, p * q, x)
        self.assertIsInstance(num, int, "The output should be an integer")

    def test_random_bit_string_generator_large_numbers(self):
        """Test if the random bit string generator produces a longer string with larger parameters."""
        # Generating a longer bit string
        bit_string_length = 100
        bit_string = NaorReingold.get_random_bits(bit_string_length)
        self.assertIsInstance(bit_string, str, "The output should be a string")
        self.assertEqual(len(bit_string), bit_string_length, "The length of the bit string should match the specified length")

    def test_get_bit_large_numbers(self):
        """Test if get_bit function generates a bit (0 or 1) with larger parameters."""
        # Using larger primes and a larger fixed number n
        n = 10
        p = 100003
        q = 100019
        x = 50000
        bit = NaorReingold.get_bit(n, p, q, x)
        self.assertIn(bit, [0, 1], "Generated bit should be either 0 or 1")

if __name__ == '__main__':
    unittest.main()
