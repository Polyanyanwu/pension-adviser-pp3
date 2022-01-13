"""enable printing of text in colors"""

from lazyme.string import color_print


def print_with_color(string_to_print, color_to_print):
    """Print the string with given color"""
    color_print(string_to_print, color=color_to_print)
