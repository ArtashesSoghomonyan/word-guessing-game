import sys
import inquirer

def choice_prompt(message, choices):
    try:
        return inquirer.prompt([inquirer.List(
            "value",
            message=message,
            choices=choices,
        )])["value"]
    except Exception as err:
        sys.exit(1)

def yes_no_prompt(message):
    try:
        return inquirer.prompt([inquirer.List(
            "value",
            message=message,
            choices=["Yes", "No"],
        )])["value"]
    except Exception as err:
        sys.exit(1)
