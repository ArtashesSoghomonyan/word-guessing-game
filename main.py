import sys
import random
import platform
import subprocess

import constants

def get_user_input():
    try:
        guess = input("Enter your guess: ")

        if guess.upper() not in constants.ALPHABET:
            return None
        else:
            return guess.upper()

    except KeyboardInterrupt:
        print("\nYou have interrupted the game.")
        sys.exit(1)

def clear_the_console():
    if platform.system() == "Windows":
        subprocess.run("cls")
    else:  # Assumes Linux/macOS/Unix
        subprocess.run("clear")

def main():
    print("Word guessing game!")

    word = "TWO_WORDS"
    state = "_" * len(word)
    tries = 3

    while True:
        clear_the_console()

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
                if state == word:
                    print("You win! 🎉")
                    break
            else:
                if tries == 1:
                    print("You lose. Try again")
                    break
                tries -= 1
        
    
if __name__ == "__main__":
    main()
