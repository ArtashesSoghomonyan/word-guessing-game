import random

from constants import *
from utils import *
from prompts import *

def main():
    print("---Word guessing game!---")

    category = choice_prompt("Pick a category for the word", CATEGORIES)

    word = random.choice(WORDS[category])
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
                    break
            else:
                if tries == 1:
                    print("You lose. Try again")
                    print(f"The word was: {word}")
                    break
                tries -= 1
    
if __name__ == "__main__":
    main()
