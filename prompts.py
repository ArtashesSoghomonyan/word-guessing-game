import inquirer

def choice_prompt(message, choices):
    return inquirer.prompt([inquirer.List(
        "value",
        message=message,
        choices=choices,
    )])["value"]

def yes_no_prompt(message):
    return inquirer.prompt([inquirer.List(
        "value",
        message=message,
        choices=["Yes", "No"],
    )])["value"]
