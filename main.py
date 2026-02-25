import sys

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

def main():
    print("Word guessing game!")

    try:
        guess = input("Enter your guess: ")

        if guess.lower() not in ALPHABET:
            print(f"Invalid input: {guess}")
        else:
            print(f"Your guess is {guess}")

    except KeyboardInterrupt:
        print("\nYou have interrupted the game.")
        sys.exit(1)

if __name__ == "__main__":
    main()
