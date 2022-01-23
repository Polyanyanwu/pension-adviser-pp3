"""
Utility module to contain general functions
1. confirm_yes_no function to display a prompt and obtain a Y or N confirmation
"""

from pension.color_prints import print_cyan, print_white, print_red


def confirm_yes_no(prompt: str):
    """
    Display a prompt and let user confirm by typing y or n

    Parameter:
        prompt(str): this will be the message that needs a Yes or No
            confirmation from user
    Returns:
        bool: True if user confirms "y" False if 'n'.
     """

    yes_no = ('y', 'n')
    print_white(f"{prompt}: ", "")
    print_cyan("('y' or 'n')", "")
    answer = input().strip().lower()

    while answer not in yes_no:
        print_red("Incorrect option: ", "")
        print_cyan("Please input 'y' or 'n'")
        print(f"{prompt}: ")
        print_cyan("('y' or 'n')")
        answer = input().strip().lower()
    if answer == 'y':
        return True
    return False
