""" Utility module to contain general functions
1. confirm_yes_no function to display a prompt and obtain a Y or N confirmation
"""

from src.color_prints import print_with_color as pc

def confirm_yes_no(prompt: str):
    """ display a prompt and let user confirm by typing y or n

        Arguments:
            prompt: this will be the message that needa a Yes or No confirmation from user
        Returns:
            boolean: True if user confirms "y" False otherwise. 
     """

    YES_NO = ('y', 'n')
    pc(f"{prompt} ('y' or 'n')", "cyan")
    answer = input().strip().lower()

    while answer not in YES_NO:
        pc("Incorrect option", "red")
        pc(f"{prompt} ('y' or 'n')", "cyan")
        answer = input().strip().lower()
    if answer == 'y':
        return True
    return False
