# RSA Algorithm

import random
import basicFunctions, MRprimalityTest, PollardsRho

# Function to check if a number is a prime using Miller-Rabin primality test
def isPrime(val):
    if MRprimalityTest.miller_rabin_test(val):
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
    ciphertext = basicFunctions.improved_fast_exponent(plaintext, e, m)  # Use fast exponential to get ciphertext
    print("Ciphertext is: ", int(ciphertext), "\n")
    return ciphertext


# Function to attempt RSA decryption without the private key
def Crack(m, e):
    if isPrime(m):  # Ensure modulus m is not a prime
        return
    p, q = PollardsRho.find_factors(m)  # Perform factorization on modulus
    if p == -1 and q == -1:  # The factorization needs to be reinitialized
        print("Quiting...")
        return -1

    phi_n = (p - 1) * (q - 1)  # Compute Euler's Totient function
    gcd, x, y = basicFunctions.extended_gcd(phi_n, e) # Extended GCD to find the private key
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
    plaintext = basicFunctions.improved_fast_exponent(ciphertext, d, m)
    print("The plaintext is: ", plaintext, "\n")
    return plaintext



# Main driver function for the RSA algorithm
def Driver():
    while True:  # Loop till user quits
        cosplay = None
        print("\n\n***************-------------------------------------***************\n")
        print("Hi! I can do RSA\n")
        print("I have a few cosplays for you to play, choose one from below\n")
        while cosplay is None:
            try:
                print("(1)Alice \n(2)Bob \n(3)Eve \n(4)Generate Keys \n(0)Quit")
                cosplay = int(input("\nPlease select a function: "))
            except ValueError:
                print("Invalid input. \n")
                continue
            if cosplay < 0 or cosplay > 4:
                print("Invalid input. \n")
                cosplay = None
                continue

        # Handle user's cosplay and call appropriate functions
        if cosplay == 0:
            print("\n")
            return
        elif cosplay == 1:
            m, e = check(1)
            Encrypt(int(m), int(e))
        elif cosplay == 2:
            m, e = check(2)
            Decrypt(int(m), int(e), True)
        elif cosplay == 3:
            m, e = check(3)
            Decrypt(int(m), int(e), False)
        elif cosplay == 4:
            getKey()

# Function to generate RSA keys based on user's cosplay of pseudorandom number generator
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
    return m, e

# Function to generate random RSA keys and a message
def genRandKey(rand_gen):
    prv_key, pub_key, message = -1, 0, 0
    m, p, q = MRprimalityTest.generate_modulus(2, rand_gen)
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

    gcd, x, y = basicFunctions.extended_gcd(phi_n, pub_key)
    prv_key = y % phi_n
    return m, pub_key, prv_key % phi_n, message

# Function to validate user input for keys
def check(cosplay):
    m, e = "m", "e"
    while not m.isdigit() or not e.isdigit():
        try:
            if cosplay == 1 or cosplay == 3:
                m, e = input("Enter public key m and e (split with space): ").split(" ")
            else:
                m, e = input("Enter private key m and e (split with space): ").split(" ")
        except ValueError:
            print("Invalid input. \n")
            continue
        if not m.isdigit() or not e.isdigit():
            print("Invalid input. \n")
            continue
    return m, e

# Driver()