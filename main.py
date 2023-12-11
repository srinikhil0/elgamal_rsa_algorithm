# BU MET CS789 Cryptography - Final project by Sri Nikhil Reddy Gudibandi
import elgamal, RSAalgorithm


def Driver():
    while True:
        choice = None
        while choice is None:
            try:
                print("\n\n***************-------------------------------------***************\n")
                print("I have a 2 algorithms for you to try, choose one from below")
                print("To try El-Gamal press '1'   \nTo try RSA press '2'   \nTo Quit press '0'")
                choice = int(input("Choose your option: "))
            except ValueError:
                print("Invalid input!")
                continue
            if choice < 0 or choice > 2:
                print("Invalid input!")
                choice = None
                continue

        if choice == 1:
            elgamal.Driver()
        elif choice == 2:
            RSAalgorithm.Driver()
        elif choice == 0:
            print("-------------------------------------\n")
            print("Quiting...")
            quit()


Driver()
