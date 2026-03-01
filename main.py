import utils
import prompts

def main():
    game_count = 1
    score = 0

    print("---Word guessing game!---")

    score += utils.session()

    print(score)

    while True:
        try_again = prompts.yes_no_prompt("Wanna play again? ")

        if try_again == "Yes":
            game_count += 1
            score += utils.session()
        else:
            print(f"You have won {score} games out of {game_count}")
            break

if __name__ == "__main__":
    main()
