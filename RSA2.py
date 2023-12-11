# RSA Algorithm

import random
from tools import basicFunctions, MRprimalityTest, PollardsRho, NaorReingold, BBS

# Function to check if a number is a prime using Miller-Rabin primality test
def isPrime(val):
    if MRprimalityTest.MillerRabinTest(val):
        print("The modulus cannot be a prime number. \n")
        return True
    else:
        return False


# Function to encrypt a plaintext message using RSA encryption
def Encrypt(m, e):
    if isPrime(m): # Check if the modulus m is not a prime
        return
    plaintext = int(input("The plaintext is: "))
    # Encrypt the plaintext using the public key (m, e)
    ciphertext = basicFunctions.FastExponent(plaintext, e, m)  # Use fast exponential to get ciphertext
    print("Ciphertext is: ", int(ciphertext), "\n")


# Function to attempt RSA decryption without the private key
def Crack(m, e):
    if isPrime(m):  # Ensure modulus m is not a prime
        return
    p, q = PollardsRho.FindFac(m)  # Perform factorization on modulus
    if p == -1 and q == -1:  # The factorization needs to be reinitialized
        print("Quiting...")
        return -1

    phi_n = (p - 1) * (q - 1)  # Compute Euler's Totient function
    gcd, x, y = basicFunctions.gcdExtended(phi_n, e) # Extended GCD to find the private key
    d = y % phi_n # Calculate the private key
    return d


# Function to decrypt a ciphertext using RSA decryption
def Decrypt(m, e, with_key):
    if isPrime(m):  # Check if the modulus m is not a prime
        return
    if with_key:
        d = e    # Incorrect use of public exponent as private key
    else:
        d = Crack(m, e)  # Attempt to crack RSA without private key
        if d == -1:
            return
    ciphertext = int(input("The ciphertext is: "))

    # Check if ciphertext and modulus are coprime
    if basicFunctions.gcd(ciphertext, m) != 1:
        print("Ciphertext is not relatively prime to the modulus.")
        return

    # Decrypt the ciphertext using the private key
    plaintext = basicFunctions.FastExponent(ciphertext, d, m)
    print("The plaintext is: ", plaintext, "\n")


# Main driver function for the RSA algorithm
def Driver():
    while True:  # Loop till user quits
        choice = None
        print("\n\n***************-------------------------------------***************\n")
        print("Hi! I can do RSA\n")
        print("I have a few functions for you to play with, choose one from below\n")
        while choice is None:
            try:
                print("(1)Encrypt \n(2)Decrypt \n(3)Crack \n(4)Generate Keys \n(5)Autorun \n(0)Quit")
                choice = int(input("\nPlease select a function: "))
            except ValueError:
                print("Invalid input. \n")
                continue
            if choice < 0 or choice > 5:
                print("Invalid input. \n")
                choice = None
                continue

        # Handle user's choice and call appropriate functions
        if choice == 0:
            print("\n")
            return
        elif choice == 1:
            m, e = check(1)
            Encrypt(int(m), int(e))
        elif choice == 2:
            m, e = check(2)
            Decrypt(int(m), int(e), True)
        elif choice == 3:
            m, e = check(3)
            Decrypt(int(m), int(e), False)
        elif choice == 4:
            getKey()
        elif choice == 5:
            autorun()

# Function to generate RSA keys based on user's choice of pseudorandom number generator
def getKey():
    rand_gen = None
    while rand_gen is None:
        try:
            print("\nWhich Pseudorandom Number Generator you wish to use?")
            print("\n(1)Naor-Reingold \n(2)Blum-Blum-Shub")
            rand_gen = int(input("\nPlease select a generator: "))
        except ValueError:
            print("Invalid input. \n")
            continue
        if rand_gen < 1 or rand_gen > 2:
            print("Invalid input. \n")
            rand_gen = None
            continue
    m, e, d, message = genRandKey(rand_gen)
    print("\nYour public key is: ( m =", m, ", e =", e, ")  \nprivate key is: ( m =", m, ", d =", d, ")")
    print("Your random message is:", message, "\n")
    return m, e

# Function to generate random RSA keys and a message
def genRandKey(rand_gen):
    prv_key, pub_key, message = -1, 0, 0
    m, p, q = MRprimalityTest.getModulus(2, rand_gen)
    phi_n = (p - 1) * (q - 1)

    # Find a public key that is coprime to phi_n
    for i in range(0, 10):
        if basicFunctions.gcd(pub_key, phi_n) == 1:
            break
        else:
            pub_key = random.randint(2, phi_n)

    # Generate a random message that is coprime to phi_n
    for i in range(0, 10):
        if basicFunctions.gcd(message, phi_n) == 1:
            break
        else:
            message = random.randint(1, m)

    gcd, x, y = basicFunctions.gcdExtended(phi_n, pub_key)
    prv_key = y % phi_n
    return m, pub_key, prv_key % phi_n, message

# Function to validate user input for keys
def check(choice):
    m, e = "m", "e"
    while not m.isdigit() or not e.isdigit():
        try:
            if choice == 1 or choice == 3:
                m, e = input("Enter public key m and e (split with space): ").split(
                    " ")
            else:
                m, e = input("Enter private key m and e (split with space): ").split(
                    " ")
        except ValueError:
            print("Invalid input. \n")
            continue
        if not m.isdigit() or not e.isdigit():
            print("Invalid input. \n")
            continue
    return m, e

# Function to automatically run the RSA encryption and decryption process
def autorun():
    print("\nStarting autorun...")
    print("Generating random keys...")
    rand_gen = random.randint(1, 2)
    m, e, d, message = genRandKey(rand_gen)
    print("Alice's public key is: ( m =", m, ", e =", e, ")")
    print("and private key is: ( m =", m, ", d =", d, ")\n")

    print("Bob wants to send message", message, "to her.")
    print("Bob encrypts the message using Alice's public key.")

    ciphertext = basicFunctions.FastExponent(message, e, m)  # Use fast exponential to get ciphertext
    print("The ciphertext is", ciphertext, "\n")

    print("Alice receives the ciphertext from Bob and decrypts it with her private key.")
    plaintext = basicFunctions.FastExponent(ciphertext, d, m)
    print("She gets the plaintext", plaintext, "\n")

    print("Eve also knows the ciphertext Bob sends to Alice;")
    print("however she does not have the private key to decrypt the message.")
    print("She tries to crack it without private key.")
    p, q = PollardsRho.FindFac(m)  # Perform factorization on modulus
    phi_n = (p - 1) * (q - 1)
    gcd, x, y = basicFunctions.gcdExtended(phi_n, e)
    d2 = y % phi_n
    print("By calculating the factor of the modulus, Eve finds", p, "and", q)
    print("which are the prime factors of the modulus", m)
    print("Eve now can have Alice's private key (", m, ",", d2, ")")
    print("and thus able to decrypt the message.")
    plaintext2 = basicFunctions.FastExponent(ciphertext, d2, m)
    print("Eve gets the result:", plaintext2, "\n")
    print("Autorun is finished.\n")


# Driver()
