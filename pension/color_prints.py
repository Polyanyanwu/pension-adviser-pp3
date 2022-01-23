"""
enable printing of text in colors
when each function is called, if a second parameter of newline
is given as "" empty string, the next print is done on same line

Idea of the functions for colors was taken from GeekforGeeks

"""


def print_red(data, newline="\n"):
    """print string data in red color """
    print(f'\033[91m {data}\033[00m', end=newline)


def print_green(data, newline="\n"):
    """print string data in green color """
    print(f"\033[92m {data}\033[00m", end=newline)


def print_yellow(data, newline="\n"):
    """print string data in yellow color """
    print(f"\033[93m {data}\033[00m", end=newline)


def print_cyan(data, newline: str = "\n"):
    """print string data in Cyan color """
    print(f"\033[96m {data}\033[00m", end=newline)


def print_blue(data, newline="\n"):
    """print string data in Blue color """
    print(f"\033[34m {data}\033[00m", end=newline)


def print_white(data, newline="\n"):
    """print string data in White color """
    print(f"\u001b[37m {data}\033[00m", end=newline)
