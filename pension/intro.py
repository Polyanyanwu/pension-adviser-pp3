"""print the initial welcome to user and request username"""

from time import sleep

from getch import getch

from pension.color_prints import print_cyan, print_white, print_yellow

from pension.username import Username
from pension.enquiries import validate_selection, confirm_entry
from pension.utils import confirm_yes_no
from pension.model import user_worksheet_exist


def introduction():
    """
    Print initial welcome message and obtain username for the user
    Returns:
        user_name(str): the validated user name
    """

    _print_intro_logo()
    sleep(2)
    print_cyan('Welcome Dear Pension Investment Enthusiast!\n')
    print_white('Do you operate a Retirement Savings Account in Nigeria? Or')
    print_white('Are you an interested person that wants to know more about')
    print_white('returns on investments of pension assets in Nigeria?')
    print_cyan("Let’s know which PFAs have best returns on pension funds\n")

    while True:
        user_name = Username().username
        if validate_existing_user(user_name):
            return user_name


def _print_intro_logo():
    """ Print the introduction logo """

    print_cyan("OOOOOOOOO    OOOOOOOOO    OO         OO           OO")
    print_white("OO     OO    OO           OO OO      OO          OO OO")
    print_cyan("OO     OO    OO           OO  OO     OO         OO   OO")
    print_white("OOOOOOOOO    OOOOOOOOO    OO   OO    OO        OO     OO")
    print_cyan("OO           OO           OO    OO   OO  OO   OO OOOOO OO  OO")
    print_white("OO           OO           OO     OO  OO      OO         OO ")
    print_cyan("OO	      OO           OO      OO OO     OO           OO")
    print_white("OO	      OOOOOOOOO    OO         OO    OO             OO\n")
    print_cyan("             THE NIGERIAN PENSION ADVISER")
    print_cyan("             ============================\n")


def print_instructions():
    """Print the instructions to guide the user """

    print()
    print_cyan("                THE INSTRUCTIONS")
    print_cyan("               ===================")
    print_white("The Pension Adviser will give you insights on the")
    print_white("performance of the Pension Industry in Nigeria.\n")
    print_white("Next you will be required to select a Fund")
    print_white("from the list of available Fund Types.")
    print_white("Select a Fund Type by inputting number listed beside it")
    print_cyan("Press any Key to continue...")
    getch()

    print_white("You will be required to input the Start Year and End Year")
    print_white("of your interest. E.g Start Year: 2016  End Year: 2018.")
    print_white("If your input spans more than one year")
    print_white("the data will be average for the period entered")
    print_white("You will be notified of the valid years from data available.")
    print_cyan("Press any Key to continue...")
    getch()

    print_white("Next you will select a Pension Fund Administrator")
    print_white("You may chose no PFA, in that case you will get")
    print_white("analysis for the entire industry without a specific PFA")
    print_white("If a PFA is selected, you will get analysis")
    print_white("for the PFA and the industry\n")


def instruction_manager():
    """
    Repeat print instructions for user until the user is okay
    """

    print_instructions()
    print_inst = True
    while print_inst:
        print_inst = confirm_yes_no("Would you like to repeat instructions?")
        if print_inst:
            print_instructions()


def main_menu():
    """
    Present menu options for the user to select
    Returns:
        menu_choice(str): inputted menu choice
    """
    _print_menu_options()
    while True:
        print_white("Please enter your choice", '')
        print_yellow("1, 2, 3, 4, or 9 : ", '')
        menu_choice = input("").lower()
        if validate_selection((1, 2, 3, 4, 9), menu_choice):
            if confirm_entry(menu_choice):
                break
            else:
                _print_menu_options()
    return menu_choice


def _print_menu_options():
    """ Display menu options to user """

    print_cyan("Please choose an option on the menu ")
    print_yellow("by inputting 1, 2, 3, 4 or 9")
    print_yellow("1: ", "")
    print("Go through the instructions")
    print_yellow("2: ", "")
    print("Print existing result of enquiries")
    print_yellow("3: ", "")
    print("Run new enquiry")
    print_yellow("4: ", "")
    print("Delete all existing enquiry results")
    print_yellow("9: ", "")
    print("Exit the application")


def validate_existing_user(user_name):
    """
    Check if user has a saved worksheet
    Parameter:
        user_name(str): the user name to check
    Returns:
        bool: True if a worksheet exists for the user or False if not
    """

    if user_worksheet_exist(user_name.lower()):
        print_yellow(f"{user_name} already exists.")
        if confirm_yes_no("Are you a returning user?"):
            return True
        else:
            print_cyan("Please chose a different user name.")
            return False
    else:
        return True
