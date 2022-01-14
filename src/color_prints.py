"""
enable printing of text in colors
when each function is called, if a second parameter of newline
is given as "" empty string,
the next print is done on same line

"""
def printRed(data, newline="\n"):
    """print string data in red color """  
    print("\033[91m {}\033[00m" .format(data), end=newline)


def printGreen(data, newline="\n"):
    """print string data in green color """  
    print("\033[92m {}\033[00m" .format(data), end=newline)


def printYellow(data, newline="\n"):
    """print string data in yellow color """  
    print("\033[93m {}\033[00m" .format(data), end=newline)


def printCyan(data, newline: str = "\n"):
    """print string data in Cyan color """  
    print("\033[96m {}\033[00m" .format(data), end=newline)


def printBlue(data, newline="\n"):
    """print string data in Blue color """  
    print("\033[34m {}\033[00m" .format(data), end=newline)


def printWhite(data, newline="\n"):
    """print string data in White color """  
    print("\u001b[37m {}\033[00m" .format(data), end=newline)
