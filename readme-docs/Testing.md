# Manual Testing

[Return to README](https://github.com/Polyanyanwu/pension-adviser-pp3/blob/cabc6a439ce92cb7939c3de84c354c45f86528d7/README.md)

- [Manual Testing](#manual-testing)
  - [**User Name**](#user-name)
  - [**Reload Application**](#reload-application)
  - [**Main Menu**](#main-menu)
  - [**Confirmation of Selection**](#confirmation-of-selection)
  - [**Go through the instructions**](#go-through-the-instructions)
  - [**PFA Selection**](#pfa-selection)

## **User Name**

- After application starts, press enter without typing a username

![No Username Entered](/readme-docs/empty_username.png)
User is informed that A user name must be entered and the prompt is displayed again

- Check for length of User name by typing characters outside of the limits of minimum 3 and and maximum 15 characters

![Username Length Test](/readme-docs/username_length.png)

The leading and training spaces are trimmed and message is displayed informing user of the violation of length of user name requirement

- Check for trimming of leading and training spaces by entering valid user name with spaces before and after the name

![Username Space Trimming Test](/readme-docs/username_spaces_trim.png)

The leading and trailing spaces are removed and user name is accepted leading to display of the welcome message

- Check for profane word in user name and if found profane word found is displayed and user is prompted for another name.

![Username Profanity Test](/readme-docs/profanity_test.png)

- Check for invalid characters (non alphanumeric characters) by inputting a user name with #.

![Username Invalid Character Test](/readme-docs/invalid_char_username.png)

A message that non alphanumeric characters detected is displayed and user is prompted to enter another name.

## **Reload Application**

Click on "Reload Program" button at anytime reloads the application and present the prompt to enter user name again.

![Reload Program](/readme-docs/reload.png)

## **Main Menu**

Test that only valid menu options are accepted. The menu is displayed after the user name has been successfully inputted.

![Main Menu](/readme-docs/menu_test.png)

First input the number 6, which is not included in any of the menu options, the error is printed asking the user to input the valid number among those displayed.

Secondly, enter the letter k, which is not a number and the error message is displayed reminding the user that an integer is expected. Enter a valid number in the options listed and the application executes the selection option.

## **Confirmation of Selection**

When the menu is displayed (same with most selection menus) and user inputs 1, a confirmation of the input is requested. 

![Confirm input](readme-docs/confirm_input.png)

If the user types a different number from the initial input, an error is displayed 

## **Go through the instructions**

When the menu is displayed and user inputs 1, a confirmation of the input is requested. If the user types 1 to confirm, the Instructions are printed in group of 5 lines. The user presses any key to advance to the next set of instructions.

![Repeat Instructions](/readme-docs/repeat_instruction_error.png)

At the prompt to Repeat Instructions, type in an character which is neither y or n, an error is printed requesting the user to input y or n. When y is inputted, the instructions are printed again. If n is inputted, the application displays the main menu once more

## **PFA Selection**

This section tests that the user is able to select any of the PFA in the list of 22 PFAs. The PFAs are presented in batches. The user is to input n to see the next set of data or p for previous. The instructions in yellow print shows the user when p or n is available. For instance, p is not available for the first set displayed.

- Check that the application accepts only the valid numbers or the p for previous and n for next and no other input.

At the prompt for selection of a PFA, type k and press enter:

![Correct PFA choice Test](/readme-docs/validate_pfa_choice.png)

The error message is displayed and user is to try again.

At the prompt type 6, which is not part of the displayed PFAs. An error message is displayed requesting the user to try again:

![PFA choice Test](/readme-docs/validate_pfa_choice_num.png)

When a number among the listed options is entered, it is accepted and the application will proceed with next actions.

- Check that the application can display next set of PFA when user types n where it is available.
Type n and press enter where the instructions include "type n to display the next list". This instruction is not visible at the last set of PFAs.

![Next set of PFA Test](/readme-docs/validate_pfa_choice_press_n.png)

The application will display the next set of PFAs and await the user further selection.

- Check that the application can display previous set of PFA when user types n where it is available.
Type p and press enter where the instructions include "type p for previous". This instruction is not visible at the first set of PFAs.

![Previous set of PFA Test](/readme-docs/validate_pfa_choice_press_p.png)

The application will display the previous set of PFAs and await further user input.
If the p is inputted where it was not available, like for the first set of PFA, the input is treated as an error as shown below.

![Previous set of PFA to start Test](/readme-docs/validate_pfa_choice_press_p_to_start.png)
