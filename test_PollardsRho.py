import unittest
import PollardsRho  

class TestPollardsRho(unittest.TestCase):

    def test_large_number_factorization(self):
        """ Test if the algorithm can factorize a relatively large composite number. """
        # Using semi-primes which are products of two large prime numbers
        number = 1000003 * 1000033  # Example large composite number
        factor = PollardsRho.pollards_rho_factorization(number)
        self.assertIn(factor, [1000003, 1000033], "Should return a non-trivial factor of the large number")

    def test_find_factors_large_number(self):
        """ Test if find_factors can find factors of a large composite number. """
        number = 1000003 * 1000033
        factors = PollardsRho.find_factors(number)
        self.assertIn(1000003, factors, "1000003 should be a factor")
        self.assertIn(1000033, factors, "1000033 should be a factor")

    def test_find_root_factor_large_number(self):
        """ Test if find_root_factor finds a root factor of a large composite number. """
        number = 1000003 * 1000033
        root_factor = PollardsRho.find_root_factor(number)
        self.assertIn(root_factor, [1000003, 1000033], "Should return a factor of the large number")

    def test_find_all_prime_factors_large_number(self):
        """ Test if find_all_prime_factors finds all prime factors of a large number. """
        number = 1000003 * 1000033
        factors = PollardsRho.find_all_prime_factors(number)
        self.assertIn(1000003, factors, "1000003 should be a prime factor")
        self.assertIn(1000033, factors, "1000033 should be a prime factor")

    def test_primitive_root_search_large_prime(self):
        """ Test if primitive_root_search finds a primitive root for a large prime number. """
        prime = 1000033  # Example large prime number
        root = PollardsRho.primitive_root_search(prime)
        self.assertTrue(PollardsRho.check_primitive_root(root, prime), "Should find a valid primitive root for a large prime")

    def test_check_primitive_root_large_prime(self):
        """ Test if check_primitive_root verifies a primitive root for a large prime. """
        prime = 1000033
        # This test requires knowing a primitive root for the large prime
        root = 2  # Assuming 2 is a primitive root; replace with a known primitive root for your prime
        self.assertTrue(PollardsRho.check_primitive_root(root, prime), "Should be a primitive root for the large prime")

if __name__ == '__main__':
    unittest.main()
