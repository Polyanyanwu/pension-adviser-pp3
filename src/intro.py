"""print the initial welcome to user and request username"""

from time import sleep

from getch import getch

from src.color_prints import print_cyan, print_white

from src.username import Username

from src.utils import confirm_yes_no


def introduction():
    """ print initial welcome message and obtain username for the user"""

    _print_intro_logo()
    sleep(3)
    print_cyan('Welcome Dear Pension Investment Enthusiast!\n')
    print('Do you operate a Retirement Savings Account in Nigeria? Or')
    print('Are you an interested person that wants to know more about')
    print('   returns on investments of pension assets in Nigeria?')
    print_cyan("Let’s find out which PFAs have best returns on pension funds\n")
    user_name = Username()
    return user_name.username


def _print_intro_logo():
    """ print the introdution logo """

    print_cyan("OOOOOOOOO     OOOOOOOOO    OO         OO           OO")
    print_white("OO     OO     OO           OO OO      OO          OO OO")
    print_cyan("OO     OO     OO           OO  OO     OO         OO   OO")
    print_white("OOOOOOOOO     OOOOOOOOO    OO   OO    OO        OO     OO")
    print_cyan("OO            OO           OO    OO   OO  OO   OO OOOOO OO  OO")
    print_white("OO            OO           OO     OO  OO      OO         OO ")
    print_cyan("OO	       OO           OO      OO OO     OO           OO")
    print_white("OO	       OOOOOOOOO    OO         OO    OO             OO\n")
    print_white("THE NIGERIAN PENSION ADVISER\n")


def print_instructions():
    """print the instructions to guide the user """

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
    """ repeat print instructions for user until the user is okay """

    print_instructions()
    print_inst = True
    while print_inst:
        print_inst = confirm_yes_no("Would you like to repeat instructions?")
        if print_inst:
            print_instructions()
