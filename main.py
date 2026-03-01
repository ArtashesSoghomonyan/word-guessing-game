import utils
import prompts

def main():
    print("---Word guessing game!---")

    utils.session()

    while True:
        try_again = prompts.yes_no_prompt("Wanna play again? ")

        if try_again == "Yes":
            utils.session()
        else:
            break

if __name__ == "__main__":
    main()
