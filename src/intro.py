"""print the initial welcome to user and request username"""

from src.color_prints import print_with_color


def introduction():
    """ print initial welcome message """

    print_with_color('Welcome Dear Pension Investment Enthusiast!\n', 'blue')
    print('Do you operate a Retirement Savings Account in Nigeria? Or')
    print('Are you an interested Nigerian that wants to know more about')
    print('   returns on investments of pension assets?')
    print('Do you operate an account with a Pension Fund Administrator?')
    print("Let’s find out which PFAs achieve best returns on pension funds.\n")
