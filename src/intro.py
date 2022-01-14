"""print the initial welcome to user and request username"""


from src.color_prints import printCyan, printBlue, printRed
from src.username import Username


def introduction():
    """ print initial welcome message and obtain username for the user"""

    printCyan('Welcome Dear Pension Investment Enthusiast!\n')
    print('Do you operate a Retirement Savings Account in Nigeria? Or')
    print('Are you an interested Nigerian that wants to know more about')
    print('   returns on investments of pension assets?')
    printCyan("Let’s find out which PFAs achieve best returns on pension funds.\n")
    user_name = Username()
    return user_name.username
