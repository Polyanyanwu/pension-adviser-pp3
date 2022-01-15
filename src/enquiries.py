""" run the enquiries the user wants on the pension returns on investment """

from getch import getch

from src.color_prints import print_cyan, print_yellow, print_white


def get_user_data(user: str):

    """ get the Fund type, years and PFA for the enquiry"""

    print_yellow("Great! Let's get started\n")
    print_cyan("Select the Fund of interest by typing", '')
    print_yellow("1, 2, 3, or 4")
    print_yellow("1: ", '')
    print_white("Fund I: Retirement Savings Account(RSA) Fund I")
    print_white("    fund for an Active Contributor who is below 50 yrs of age")
    print_white("    and chooses for contribution to be invested in this fund")
    print_yellow("2: ", '')
    print_white("Fund II: Default fund for all Active Contributors who are")
    print_white("    below 50 yrs of age")
    print_yellow("3: ", '')
    print_white("Fund III: Default fund for all Active Contributors who are")
    print_white("    50 yrs and above")
    print_yellow("4: ", '')
    print_white("Fund IV:  RSA Fund for Retirees only")

    while True:
        print_white("Please enter your choice", '')
        print_yellow("1, 2, 3, or 4")
        fund_choice = input("")
        if validate_fund_choice(fund_choice):
            if confirm_entry(fund_choice):
                print("Choice is okay!")
                break
    return user


def validate_fund_choice(fund_choice):
    """ validate the choice is number 1, to 4 """
    choices = (1, 2, 3, 4)
    try:
        choice = int(fund_choice)
        if choice not in choices:
            raise ValueError(
                f"Your input must be 1, 2, 3 or 4: you provided {choice}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def confirm_entry(string_entered):
    """ confirm that data entered is same as to be entered """

    print_yellow(f"Confirm your entry by typing {string_entered} again", '')
    new_input = input()
    if str(string_entered) != new_input:
        print_yellow(f"Your entry {string_entered}\
             is different from your confirmation {new_input}")
        print_cyan("Press any Key to try again...")
        getch()
        return False
    return True
