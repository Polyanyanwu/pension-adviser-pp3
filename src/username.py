"""Receives user name input and carry out validation"""

from better_profanity import profanity  # ensure profane words are disallowed
from src.color_prints import print_with_color


class Username():
    """Create a Username object

    Returns a validated username entered by the user
    """

    def __init__(self):
        self.username = self._input_username()

    def _validate_username(self,  user_name: str):
        """Checks username input is valid
          
        Arguments:
            user_name: The string input typed in by the user to be validated
        Returns:
            boolean: True when validated or false if not validated
        """

        try:
            if not user_name:
                raise ValueError("A user name must be entered")
            if not "".join(user_name.split()).isalnum():
                raise ValueError("Invalid characters detected")
            if profanity.contains_profanity(user_name):
                raise ValueError("Profane word found")
            if len(user_name) > 15 or len(user_name) < 3:
                raise ValueError("Length of User name mut be between 3 and 15")

        except ValueError as e:
            print_with_color(f"Invalid username {user_name}: {e}, please try again.\n")
            return False

        return True

    def _input_username(self):
        """ Function to enable user to input a username
        The name should be with alphanumeric characters and spaces.
        The function checks for profane words using `better_profanity. 
        The prompt for username is repeated until valid username is inputed

        Returns:
            string of validated username
        """

        while True:
            print_with_color("Letters A-Z, a-z, numbers 0-9 and spaces are allowed.")
            print("Username whould not exceed 15 characters, leading and training spaces will be removed.")
            user_name = input("Please type in a user name:\n")
            if self._validate_username(user_name):
                break

        return user_name.strip()

