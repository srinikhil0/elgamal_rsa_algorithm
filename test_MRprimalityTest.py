import unittest
import random
import basicFunctions

# Assuming the provided BBS code snippet is stored in a file named BBS.py
# Including the provided Blum-Blum-Shub code directly here for testing purposes
def find_initial_value(num):
    while True:
        initial_value = random.randint(1, num)
        if basicFunctions.gcd(initial_value, num) == 1:
            return initial_value

def get_bit(modulus):
    initial_value = find_initial_value(modulus)
    s = initial_value
    bits = []
    for _ in range(modulus):
        s = (s ** 2) % modulus
        bits.append(s % 2)
    return bits[-1]

def generate_random_bits(count, p, q):
    modulus = p * q
    return ''.join(str(get_bit(modulus)) for _ in range(count))

def random_number_generator():
    bits = generate_random_bits(24, 11, 23)  # 24-bit number, p=11, q=23
    return int(bits, 2)

# Unit tests for Blum-Blum-Shub algorithm
class TestBlumBlumShub(unittest.TestCase):

    def test_get_bit(self):
        """ Test if get_bit function generates a bit (0 or 1). """
        modulus = 11 * 19  # Example modulus with two prime numbers
        bit = get_bit(modulus)
        self.assertIn(bit, [0, 1], "Generated bit should be either 0 or 1")

    def test_generate_random_bits(self):
        """ Test if generate_random_bits function generates a string of bits. """
        count = 10
        p, q = 11, 19  # Example prime numbers
        bits = generate_random_bits(count, p, q)
        self.assertEqual(len(bits), count, f"Should generate a string of {count} bits")
        for bit in bits:
            self.assertIn(bit, ['0', '1'], "Each character should be '0' or '1'")

    def test_random_number_generator(self):
        """ Test if random_number_generator generates a number within expected range. """
        num = random_number_generator()
        self.assertIsInstance(num, int, "Generated value should be an integer")
        self.assertGreaterEqual(num, 0, "Generated number should be non-negative")
        self.assertLess(num, 2**24, "Generated number should be less than 2^24")

if __name__ == '__main__':
    unittest.main()

