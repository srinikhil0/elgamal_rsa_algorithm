import unittest
import basicFunctions
import BBS  

class TestBlumBlumShub(unittest.TestCase):

    def test_find_initial_value_medium_number(self):
        """Test if find_initial_value returns a value relatively prime to a medium-sized number."""
        num = 100003 * 10007  # Medium-sized composite number
        value = BBS.find_initial_value(num)
        self.assertEqual(basicFunctions.gcd(value, num), 1, "Returned value should be relatively prime to num")

    def test_get_bit_medium_modulus(self):
        """Test if get_bit function generates a bit (0 or 1) with a medium modulus."""
        modulus = 100003 * 10007  # Medium modulus
        bit = BBS.get_bit(modulus)
        self.assertIn(bit, [0, 1], "Generated bit should be either 0 or 1")

    def test_generate_random_bits_medium_modulus(self):
        """Test if generate_random_bits function generates a string of bits with a medium modulus."""
        count = 50  # Number of bits to generate
        p, q = 100003, 10007  # Medium prime numbers
        bits = BBS.generate_random_bits(count, p, q)
        self.assertEqual(len(bits), count, "Should generate a string of length equal to count")
        for bit in bits:
            self.assertIn(bit, ['0', '1'], "Each character should be '0' or '1'")

    def test_random_number_generator_medium_modulus(self):
        """Test if random_number_generator generates a number within the expected range for a medium modulus."""
        num = BBS.random_number_generator()
        self.assertIsInstance(num, int, "Generated value should be an integer")
        self.assertGreaterEqual(num, 0, "Generated number should be non-negative")
        self.assertLess(num, 2**24, "Generated number should be less than 2^24")

if __name__ == '__main__':
    unittest.main()
