import elgamal, RSAalgorithm

def Driver():
    """Main driver function for selecting and executing cryptographic algorithms.

    This function presents the user with a choice of trying out either the
    ElGamal algorithm or the RSA algorithm. Based on the user's choice, it
    calls the respective driver function from the imported modules.
    """
    while True:
        choice = None
        while choice is None:
            try:
                # Display the options to the user
                print("\n\n***************-------------------------------------***************\n")
                print("I have 2 algorithms for you to try, choose one from below")
                print("To try El-Gamal press '1'\nTo try RSA press '2'\nTo Quit press '0'")
                choice = int(input("Choose your option: "))
            except ValueError:
                # Handle non-integer inputs
                print("Invalid input!")
                continue
            if choice < 0 or choice > 2:
                # Handle out-of-range inputs
                print("Invalid input!")
                choice = None
                continue

        # Execute the chosen algorithm or quit
        if choice == 1:
            elgamal.Driver()  # Execute ElGamal algorithm
        elif choice == 2:
            RSAalgorithm.Driver()  # Execute RSA algorithm
        elif choice == 0:
            # Exit the program
            print("-------------------------------------\n")
            print("Quitting...")
            quit()

# Run the main driver function
Driver()
