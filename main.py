import sys
import random
import platform
import subprocess

import inquirer

from constants import *

def get_user_input():
    try:
        guess = input("Enter your guess: ")

        if guess.upper() not in ALPHABET:
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
    print("---Word guessing game!---")

    category = inquirer.prompt([inquirer.List(
        "value",
        message="Pick a category for the word",
        choices=CATEGORIES,
    )])

    word = random.choice(WORDS[category["value"]])
    state = "_" * len(word)
    tries = 3

    while True:
        clear_the_console()

        print(f"Category: {category["value"]}")
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
