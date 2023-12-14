import unittest

from basicFunctions import is_odd, gcd, multiplicative_inverse, basic_fast_exponent, improved_fast_exponent, extended_gcd

class TestCryptographicFunctions(unittest.TestCase):

    def test_is_odd(self):
        self.assertTrue(is_odd(1000001), "1000001 should be odd")
        self.assertFalse(is_odd(1000002), "1000002 should not be odd")

    def test_gcd_large_numbers(self):
        self.assertEqual(gcd(1000000007, 1000000009), 1, "GCD of two large primes should be 1")

    def test_multiplicative_inverse_large(self):
        mod = 1000000007  # A large prime number
        x = 123456789
        inverse = multiplicative_inverse(x, mod)
        self.assertNotEqual(inverse, -1, "Inverse should exist for a non-zero number modulo a prime")
        self.assertEqual((x * inverse) % mod, 1, "The multiplicative inverse should satisfy the condition (x * inverse) % mod == 1")

    def test_basic_fast_exponent_large_numbers(self):
        self.assertEqual(basic_fast_exponent(2, 1000000, 1000000007), pow(2, 1000000, 1000000007), "Basic fast exponentiation should match Python's pow function result")

    def test_improved_fast_exponent_large_numbers(self):
        self.assertEqual(improved_fast_exponent(2, 1000000, 1000000007), pow(2, 1000000, 1000000007), "Improved fast exponentiation should match Python's pow function result")

    def test_extended_gcd_large_numbers(self):
        a, b = 1000000007, 1000000009
        gcd_value, x, y = extended_gcd(a, b)
        self.assertEqual(gcd_value, 1, "GCD of two large primes should be 1")
        self.assertEqual(a * x + b * y, 1, "Extended GCD should satisfy the equation ax + by = gcd(a, b)")

if __name__ == '__main__':
    unittest.main()
