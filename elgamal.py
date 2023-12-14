# El-Gamal algorithm implementation
# Includes functions for generating public information, encryption, decryption, and eavesdropping

import random
import basicFunctions, MRprimalityTest, BBstepGNstep, BBS, NaorReingold, PollardsRho

# Function to generate public information for Alice
def alice_public_information(rand_gen, r):
    max_prime = 0
    # Generate 5 prime numbers using Miller-Rabin primality test and select the largest
    primes = MRprimalityTest.generate_primes(5, rand_gen)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    p = max_prime

    # Generate one of the primitive roots of p
    b = PollardsRho.primitive_root_search(p)

    # Generate a random number r if not provided
    if r is None:
        r = MRprimalityTest.generate_primes(1, rand_gen)[0] % p - 1

    # Calculate b raised to the power of r modulo p
    br = basicFunctions.improved_fast_exponent(b, r, p)
    print(f"Public information:\nAlice's prime number: {p}\nGenerator: {b}\nPublic key: {br}")
    print(f"\nKeep Alice's secret key: {r}")

# Function to generate public information for Bob
def bob_pub_info(rand_gen, r):
    # # Generate a random number l if not provided

    max_prime = 0
    # Generate 5 prime numbers using Miller-Rabin primality test and select the largest
    primes = MRprimalityTest.generate_primes(5, rand_gen)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    p = max_prime

    # Generate one of the primitive roots of p
    b = PollardsRho.primitive_root_search(p)

    # Generate a random number r if not provided
    if r is None:
        r = MRprimalityTest.generate_primes(1, rand_gen)[0] % p - 1

    # Calculate b raised to the power of r modulo p
    br = basicFunctions.improved_fast_exponent(b, r, p)
    print(f"Public information:\nBob's prime number: {p}\nGenerator: {b}\nPublic key: {br}")
    print(f"\nKeep Bob's secret key: {r}")

# Function to encrypt a message using El-Gamal encryption
def encrypt(g, h, message, p):
    """
    Encrypt a message using ElGamal encryption.

    Parameters:
    g (int): A primitive root modulo p.
    h (int): The recipient's public key (h = g^x mod p).
    message (int): The plaintext message to be encrypted.
    p (int): A large prime number.

    Returns:
    tuple: A pair (c1, c2) representing the encrypted message.
    """
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(h, k, p)) % p
    return (c1, c2)

# Function to decrypt a message using El-Gamal decryption
def decrypt(c1, c2, x, p):
    """
    Decrypt a message using ElGamal decryption.

    Parameters:
    c1 (int): The first component of the ciphertext.
    c2 (int): The second component of the ciphertext.
    x (int): The recipient's private key.
    p (int): A large prime number.

    Returns:
    int: The decrypted plaintext message.
    """
    s = pow(c1, x, p)
    s_inv = basicFunctions.multiplicative_inverse(s, p)
    message = (c2 * s_inv) % p
    return message

# Interactive function for Alice to generate public information or encrypt a message
def alice():
    choice = None
    while choice is None:
        try:
            print("\nYou have chosen Alice")
            choice = int(input("\nAlice can do two things: \n1 - Get public information \n2 - Encrypt a message\nWhat do you want to choose? "))
            if choice not in [1, 2]:
                raise ValueError()
        except ValueError:
            print("Invalid input. \n")
            choice = None

    if choice == 1:
        # Generate Alice's public information
        print("\n*** Generating Secret Key ***\n")
        r = None
        alice_public_information(2, r)

    elif choice == 2:
        # Encrypt a message as Alice
        p, message, bl, g = None, None, None, None
        while None in [p, message, bl, g]:
            try:
                message = int(input("\nEnter the message you want to send: "))
                bl = int(input("Enter Bob's public Key (h): "))
                g = int(input("Enter the generator (g): "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input. \n")
        
        # Encrypt message
        c1, c2 = encrypt(g, bl, message, p)
        print(f"The ciphertext is (c1, c2): ({c1}, {c2})\n")

# Interactive function for Bob to generate public information or decrypt a message
def bob():
    choice = None
    while choice is None:
        try:
            choice = int(input("Do you wish to \n(1) Get public info \n(2) Decrypt a message: \n Enter you choice: "))
            if choice not in [1, 2]:
                raise ValueError()
        except ValueError:
            print("Invalid input. \n")
            choice = None

    if choice == 1:
        # Generate Bob's public information
        print("\n*** Generating Secret Key ***\n")
        r = None
        bob_pub_info(2, r)

    elif choice == 2:
        # Decrypt a message as Bob
        p, c1, c2, x = None, None, None, None
        while None in [p, c1, c2, x]:
            try:
                c1 = int(input("Enter the first component of the ciphertext (c1): "))
                c2 = int(input("Enter the second component of the ciphertext (c2): "))
                x = int(input("Enter Bob's secret Key: "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input.")
        
        # Decrypt message
        message = decrypt(c1, c2, x, p)
        print(f"The decrypted message is: {message}\n")

# Interactive function for Eve to attempt to eavesdrop and decrypt a message
def eve():
    p, c1, c2, b, bl = None, None, None, None, None
    while None in [p, c1, c2, b, bl]:
        try:
            c1 = int(input("Enter the first component of the ciphertext (c1): "))
            c2 = int(input("Enter the second component of the ciphertext (c2): "))
            b = int(input("Enter the generator: "))
            bl = int(input("Enter public Key: "))
            p = int(input("Enter the prime number: "))
        except ValueError:
            print("Invalid input.")

    # Attempt to retrieve private keys using Baby-Step Giant-Step algorithm
    x = BBstepGNstep.baby_step_giant_step(b, bl, p)

    # Check if a valid discrete logarithm was found
    if x == -1:
        print("Failed to crack the secret key using Baby-Step Giant-Step.")
        return

    # Crack the ciphertext
    message = decrypt(c1, c2, x, p)

    print(f"The secret Key involved is: {x}")
    print(f"The decrypted message is: {message}\n")

# Main function to drive the El-Gamal algorithm, allowing users to choose roles
def Driver():
    while True:
        cosplay = None
        print("\n***************-------------------------------------***************\n")
        print("Welcome to the El-Gamal algorithm simulation!")
        print("Choose a role to play:")
        while cosplay is None:
            try:
                print("1 - Alice \n2 - Bob \n3 - Eve \n0 - Quit")
                cosplay = int(input("Which role do you want to play? "))
                if cosplay not in range(5):
                    raise ValueError()
            except ValueError:
                print("Invalid input. \n")
                cosplay = None

        if cosplay == 1:
            alice()
        elif cosplay == 2:
            bob()
        elif cosplay == 3:
            eve()
        elif cosplay == 0:
            print("\nExiting the program.")
            return

# Driver()