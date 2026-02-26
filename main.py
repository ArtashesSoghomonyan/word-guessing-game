import sys
import constants

def get_user_input():
    try:
        guess = input("Enter your guess: ")

        if guess.lower() not in constants.ALPHABET:
            return None
        else:
            return guess

    except KeyboardInterrupt:
        print("\nYou have interrupted the game.")
        sys.exit(1)


def main():
    print("Word guessing game!")
    
    while True:
        guess = get_user_input()
        
        if guess == None:
            print("Invalid input!")
        else:
            print(guess)
    
if __name__ == "__main__":
    main()
