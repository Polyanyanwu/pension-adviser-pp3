"""print the initial welcome to user and request username"""


from src.color_prints import printCyan, printYellow, printRed, printWhite

from src.username import Username

from time import sleep

import getch

from src.utils import confirm_yes_no


def introduction():
    """ print initial welcome message and obtain username for the user"""

    _print_intro_logo()
    sleep(3)
    printCyan('Welcome Dear Pension Investment Enthusiast!\n')
    print('Do you operate a Retirement Savings Account in Nigeria? Or')
    print('Are you an interested person that wants to know more about')
    print('   returns on investments of pension assets in Nigeria?')
    printCyan("Let’s find out which PFAs achieve best returns on pension funds.\n")
    user_name = Username()
    return user_name.username

def _print_intro_logo():
    """ print the introdution logo """

    printCyan("OOOOOOOOO     OOOOOOOOO    OO         OO           OO")
    printWhite("OO     OO     OO           OO OO      OO          OO OO")
    printCyan("OO     OO     OO           OO  OO     OO         OO   OO")
    printWhite("OOOOOOOOO     OOOOOOOOO    OO   OO    OO        OO     OO")
    printCyan("OO            OO           OO    OO   OO  OO   OO OOOOO OO  OO")
    printWhite("OO            OO           OO     OO  OO      OO         OO ")
    printCyan("OO	       OO           OO      OO OO     OO           OO")
    printWhite("OO	       OOOOOOOOO    OO         OO    OO             OO\n")
    printWhite("THE NIGERIAN PENSION ADVISER\n")

def print_instructions():
    """print the instructions to guide the user """

    printCyan("                THE INSTRUCTIONS")
    printCyan("               ===================")
    printWhite("The Pension Adviser will give you insights on the performance")
    printWhite("of the Pension Industry in Nigeria.\n")
    printWhite("You will be required to input the Start Year and End Year")
    printWhite("of your interest. E.g Start Year: 2016  End Year: 2018.")
    printWhite("If your input spans more than one year")
    printWhite("the data will be average for the period entered")
    printWhite("You will be notified of the valid years from data available.")
    printCyan("Press any Key to continue...")
    getch.getch()
    printWhite("Next you will be required to select a Fund")
    printWhite("from the list of available Fund Types.")
    printWhite("Select a Fund Type by inputting number listed beside the fund")
    printCyan("Press any Key to continue...")
    getch.getch()
    printWhite("Next you will select a Pension Fund Administrator")
    printWhite("You may chose no PFA, in that case you will get")
    printWhite("analysis for the entire industry without a specific PFA")
    printWhite("If a PFA is selected, you will get analysis")
    printWhite("for the PFA and the industry")


def instruction_manager():
    """ repeat print instructions for user until the user is okay """
    print_instructions()
    print_instruc = True
    while print_instruc:
        print_instruc = confirm_yes_no("Would you like to repeat the instructions?")
        if print_instruc:
            print_instructions()
