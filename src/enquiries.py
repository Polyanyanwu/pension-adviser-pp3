""" run the enquiries the user wants on the pension returns on investment """

from getch import getch

from src.color_prints import printCyan, printYellow, printWhite


def get_user_data(user: str):

    """ get the Fund type, years and PFA for the enquiry"""

    printYellow("Great! Let's get started\n")
    printCyan("Select the Fund of interest by typing", '')
    printYellow("1, 2, 3, or 4")
    printYellow("1: ", '')
    printWhite("Fund I: Retirement Savings Account(RSA) Fund I")
    printWhite("    fund for an Active Contributor who is below 50 yrs of age")
    printWhite("    and chooses for contribution to be invested in this fund")
    printYellow("2: ", '')
    printWhite("Fund II: Default fund for all Active Contributors who are")
    printWhite("    below 50 yrs of age")
    printYellow("3: ", '')
    printWhite("Fund III: Default fund for all Active Contributors who are")
    printWhite("    50 yrs and above")
    printYellow("4: ", '')
    printWhite("Fund IV:  RSA Fund for Retirees only")

    while True:
        printWhite("Please enter your choice", '')
        printYellow("1, 2, 3, or 4")
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

    printYellow(f"Confirm your entry by typing {string_entered} again", '')
    new_input = input()
    if str(string_entered) != new_input:
        printYellow(f"Your entry {string_entered} is different from your confirmation {new_input}")
        printCyan("Press any Key to try again...")
        getch()
        return False
    return True
