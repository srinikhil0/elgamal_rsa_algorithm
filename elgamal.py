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
    print(f"Public information:\nAlice's prime number: {p}\nGenerator: {b}\nPublic number: {br}.")
    print(f"\nKeep Alice's secret number: {r}")

# Function to generate public information for Bob
def bob_pub_info(p, b, l):
    # Generate a random number l if not provided
    if l is None:
        l = MRprimalityTest.generate_primes(1, 2)[0] % p - 1

    # Calculate b raised to the power of l modulo p
    bl = basicFunctions.improved_fast_exponent(b, l, p)
    print(f"Bob's public number is: {bl}")
    print(f"Bob's secret number is: {l}, please keep it secret.\n")

# Function to encrypt a message using El-Gamal encryption
def encrypt(brl, message, p):
    return (message * brl) % p

# Function to decrypt a message using El-Gamal decryption
def decrypt(brl_rev, cipher, p):
    return (cipher * brl_rev) % p

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
        print("\n*** Generating Secret Number ***\nIf you want to create your own secret number, press 'y'.\nOtherwise, press 'n' and we will generate it for you.")
        rand = input("\nEnter your own secret key? (y/n): ").lower()
        r = None
        if rand == "y":
            while r is None:
                try:
                    r = int(input("\nEnter Alice's secret number: "))
                except ValueError:
                    print("Invalid input.")
        else:
            r = None
        alice_public_information(2, r)
    elif choice == 2:
        # Encrypt a message as Alice
        p, message, bl, r = None, None, None, None
        while None in [p, message, bl, r]:
            try:
                message = int(input("\nEnter the message you want to send: "))
                bl = int(input("Enter the public Key for Bob: "))
                r = int(input("Enter Alice's secret Key: "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input. \n")
        brl = basicFunctions.improved_fast_exponent(bl, r, p)
        cipher = encrypt(brl, message, p)
        print(f"The ciphertext is {cipher}\n")

# Interactive function for Bob to generate public information or decrypt a message
def bob():
    choice = None
    while choice is None:
        try:
            choice = int(input("Do you wish to \n(1) Get public info \n(2) Decrypt a message: "))
            if choice not in [1, 2]:
                raise ValueError()
        except ValueError:
            print("Invalid input. \n")
            choice = None

    if choice == 1:
        # Generate Bob's public information
        print("\nEnter Alice's public info below (split with space)")
        p, b, br = None, None, None
        while None in [p, b, br]:
            try:
                p, b, br = input("Prime Number, Generator, Public Number: ").split(" ")
                if not all(x.isdigit() for x in [p, b, br]):
                    raise ValueError()
                p, b, br = int(p), int(b), int(br)
                if not MRprimalityTest.miller_rabin_test(p):
                    print(f"{p} is not a prime number.\n")
                    return
            except ValueError:
                print("Invalid input. \n")
                p, b, br = None, None, None

        rand = None
        while rand not in ["y", "n"]:
            try:
                rand = input("Enter your own secret number? (y/n): ").lower()
            except ValueError:
                print("Invalid input. \n")

        l = None
        if rand == "y":
            while l is None:
                try:
                    l = int(input("Enter Bob's secret key: "))
                except ValueError:
                    print("Invalid input.")
        else:
            l = None
        bob_pub_info(p, b, l)

    elif choice == 2:
        # Decrypt a message as Bob
        p, cipher, br, l = None, None, None, None
        while None in [p, cipher, br, l]:
            try:
                cipher = int(input("Enter the ciphertext: "))
                br = int(input("Enter public number for Alice: "))
                l = int(input("Enter Bob's secret number: "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input.")
        brl = basicFunctions.improved_fast_exponent(br, l, p)
        gcd, x, y = basicFunctions.extended_gcd(p, brl)
        brl_rev = y % p
        message = decrypt(brl_rev, cipher, p)
        print(f"The message is {message}\n")

# Interactive function for Eve to attempt to eavesdrop and decrypt a message
def eve():
    p, cipher, b, br, bl = None, None, None, None, None
    while None in [p, cipher, b, br, bl]:
        try:
            cipher = int(input("Enter the ciphertext: "))
            b = int(input("Enter the generator: "))
            br = int(input("Enter Alice's public number: "))
            bl = int(input("Enter Bob's public number: "))
            p = int(input("Enter the prime number: "))
        except ValueError:
            print("Invalid input.")

    # Attempt to retrieve private keys using Baby-Step Giant-Step algorithm
    r = BBstepGNstep.baby_step_giant_step(br, b, p)
    l = BBstepGNstep.baby_step_giant_step(bl, b, p)

    # Crack the ciphertext
    brl = basicFunctions.improved_fast_exponent(br, l, p)
    gcd, x, y = basicFunctions.extended_gcd(p, brl)
    brl_rev = y % p
    message = decrypt(brl_rev, cipher, p)

    print(f"Alice's secret number is: {r}")
    print(f"Bob's secret number is: {l}")
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
                print("1 - Alice \n2 - Bob \n3 - Eve \n4 - Autorun \n0 - Quit")
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
        elif cosplay == 4:
            autorun()
        elif cosplay == 0:
            print("\nExiting the program.")
            return

# Function to automatically run the entire El-Gamal process
def autorun():
    max_prime, b = 0, 0
    rand_gen = random.randint(1, 2)

    print("\nStarting automatic run...")
    print("Generating a random prime number...")
    primes = MRprimalityTest.generate_primes(5, rand_gen)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    p = max_prime

    # Generate a primitive root of p
    b = PollardsRho.primitive_root_search(p)

    # Generate random numbers r and l
    r = MRprimalityTest.generate_primes(1, rand_gen)
    r = r[0] % p - 1
    l = MRprimalityTest.generate_primes(1, rand_gen)
    l = l[0] % p - 1

    # calculate b^r
    br = basicFunctions.improved_fast_exponent(b, r, p)
    bl = basicFunctions.improved_fast_exponent(b, l, p)
    brl = basicFunctions.improved_fast_exponent(br, l, p)
    gcd, x, y = basicFunctions.extended_gcd(p, brl)
    brl_rev = y % p

    print("Alice and Bob both agreed on prime number", p, "and the generator", b)
    print("Alice chooses her secret number", r, "and calculates", br)
    print("Bob chooses his secret number", l, "and calculates", bl, "\n")
    print("--------------------------")
    print("The public knowledge are")
    print("Prime number:", p)
    print("The generator:", b)
    print("Alice's public number:", br)
    print("Bob's public number:", bl)
    print("--------------------------")
    print("The private knowledge are")
    print("Alice's secret number:", r)
    print("Bob's secret number:", l)
    print("Alice and Bob both share the key:", brl)
    print("And the multi-inverse of the key:", brl_rev)
    print("--------------------------\n")
    print("Now Alice and Bob can share messages between them.\n")

    if rand_gen == 1:
        message = NaorReingold.random_number_generator()
    elif rand_gen == 2:
        message = BBS.random_number_generator()
    print("Alice wants to send the message:", message, "to Bob.")
    cipher = (message * brl) % p
    plain = (cipher * brl_rev) % p
    print("She does the calculation:", message, "*", brl, "mod", p, "=", cipher)
    print("Bob receives the cipher and does the calculation:", cipher, "*", brl_rev, "mod", p, "=", plain)
    print("They successfully exchanged information.\n")

    print("Eve also knows the public information and the ciphertext.")
    print("She will try to crack it without knowing the secret numbers.")
    print("She is trying...(usually under 10 sec with a 24-bit number)")
    r2 = BBstepGNstep.baby_step_giant_step(br, b, p)
    l2 = BBstepGNstep.baby_step_giant_step(bl, b, p)
    plaintext2 = decrypt(brl_rev, cipher, p)
    print("By using Baby-Step&Giant-Step, Eve tries to solve the problem.")
    print("She now has the secret numbers:", r2, "and", l2)
    print("With that, she is able to get the plaintext:", plaintext2, "\n")
    print("Autorun is finished.\n")


# Driver()
