import sys
import platform
import subprocess

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
