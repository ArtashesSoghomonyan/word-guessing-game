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

    word = "guess"
    state = "_" * len(word)
    tries = 3

    while True:
        if state == word:
            print("You win! 🎉")

        print(state)
        print(f"Tries left: {tries}")

        guess = get_user_input()

        if guess == None:
            print("Invalid input!")
        else:
            # Replacing state with guessed character
            # for example _____ -> __e__ (word = guess) 

            if guess in word:
                for index, char in enumerate(word):
                    if char == guess:
                        state = state[:index] + char + state[index + 1:]
            else:
                if tries == 1:
                    print("You lose. Try again")
                    sys.exit(1)
                tries -= 1
        
        print("###########################")

    
if __name__ == "__main__":
    main()
