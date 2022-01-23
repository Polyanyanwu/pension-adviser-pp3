"""Receive user name input and carry out validation"""

from better_profanity import profanity  # ensure profane words are disallowed

from pension.color_prints import print_cyan, print_red, print_white


class Username:
    """
    Create a User name object
    Returns a validated user name entered by the user
    """

    def __init__(self):
        self.username = self._input_username()

    def _validate_username(self,  user_name: str):
        """
        Checks user name input is valid
        Name should be between 3 and 15 characters long.
        The function checks for profane words using `better_profanity.
        Parameters:
            user_name(str): The string input typed in
            by the user to be validated
        Returns:
            bool: True when validated or false if not validated
        """

        try:
            if not user_name:
                raise ValueError("A user name must be entered")
            user_name = user_name.strip()
            if len(user_name) > 15 or len(user_name) < 3:
                raise ValueError("Length of User name mut be between 3 and 15")
            if not ''.join(user_name.split()).isalnum():
                raise ValueError("Non alphanumeric characters detected")
            if profanity.contains_profanity(user_name):
                raise ValueError("Profane word found")

        except ValueError as val_error:
            print_red(f"Invalid user name {user_name}:", "")
            print(f"{val_error}, please try again.\n")
            return False

        return True

    def _input_username(self):
        """
        Function to enable user to input a user name
        The prompt for username is repeated until valid username is inputted
        Returns:
            string of validated username
        """

        while True:
            print_white("Let's meet you, enter a user name")
            print_cyan("A-Z, a-z, 0-9 & spaces are permitted")
            print_cyan("User name should be between 3 and 15 characters")
            print_cyan("leading & trailing spaces will be removed.")
            user_name = input(" Please type in a user name: ")
            if self._validate_username(user_name):
                break

        return user_name.strip()
