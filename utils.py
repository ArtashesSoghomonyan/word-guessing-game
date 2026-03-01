import sys
import random
import platform
import subprocess

import constants
import prompts

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

def session():
    category = prompts.choice_prompt("Pick a category for the word", constants.CATEGORIES)
    word = random.choice(constants.WORDS[category])

    state = "_" * len(word)
    tries = 3

    while True:
        clear_the_console()

        print(f"Category: {category}")
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
                    return 1
            else:
                if tries == 1:
                    print("You lose. Try again")
                    print(f"The word was: {word}")
                    return 0
                tries -= 1

