""" run the enquiries the user wants on the pension returns on investment """


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
    return user
