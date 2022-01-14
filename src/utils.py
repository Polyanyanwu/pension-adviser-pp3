"""
Utility module to contain general functions
1. confirm_yes_no function to display a prompt and obtain a Y or N confirmation
"""

from src.color_prints import printCyan, printWhite, printRed

def confirm_yes_no(prompt: str):
    """ display a prompt and let user confirm by typing y or n

        Arguments:
            prompt: this will be the message that needa a Yes or No confirmation from user
        Returns:
            boolean: True if user confirms "y" False if 'n'.
     """

    YES_NO = ('y', 'n')
    printWhite(f"{prompt}: ","")
    printCyan("('y' or 'n')")
    answer = input().strip().lower()

    while answer not in YES_NO:
        printRed("Incorrect option: ", "")
        printCyan("Please input 'y' or 'n'")
        print(f"{prompt}: ")
        printCyan("('y' or 'n')")
        answer = input().strip().lower()
    if answer == 'y':
        return True
    return False
