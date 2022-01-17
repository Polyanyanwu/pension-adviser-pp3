## **User Name**
* After application starts, press enter without typing a username
![No Username Entered](/readme-docs/empty_username.png)
User is informed that A user name must be entered and the prompt is displayed again

* Check for length of User name by typing characters outside of the limits of minimum 3 and and maximum 15 characters
![Username Length Test](/readme-docs/username_length.png)
The leading and training spaces are trimmed and message is displayed informing user of the violation of length of user name requirement

* Check for trimming of leading and training spaces by entering valid user name with spaces before and after the name
![Username Space Trimming Test](/readme-docs/username_spaces_trim.png)
The leading and trailing spaces are removed and user name is accepted leading to display of the welcome message

* Check for profane word in user name and if found profane word found is displayed and user is prompted for another name.
![Username Prafanity Test](/readme-docs/profanity_test.png)


* Check for invalid characters (non alphanumeric characters) by inputting a user name with #.
![Username Invalid Character Test](/readme-docs/invalid_char_username.png)
A message that non alphanumeric characters detected is displayed and user is prompted to enter another name.

## **PFA Selection**
This section tests that the user is able to select any of the PFA in the list of 22 PFAs. The PFAs are presented in batches. The user is to input n to see the next set of data or p for previous. The instructions in yellow print shows the user when p or n is available. For instance, p is not available for the first set displayed.

* Check that the application accepts only the valid numbers or the p for previous and n for next and no other input.

At the prompt for selection of a PFA, type k and press enter:

![Correct PFA choice Test](/readme-docs/validate_pfa_choice.png)
The error message is displayed and user is to try again.

At the prompt type 6, which is not part of the displayed PFAs. An error message is displayed requesting the user to try again:

![PFA choice Test](/readme-docs/validate_pfa_choice_num.png)
When a number among the listed options is entered, it is accepted and the application will proceed with next actions.

* Check that the application can display next set of PFA when user types n where it is available. 
Type n and press enter where the instructions iclude "type n to display the next list". This instruction is not visible at the last set of PFAs.

![Next set of PFA Test](/readme-docs/validate_pfa_choice_press_n.png)
The application will display the next set of PFAs and await the user further selection.

* Check that the application can display previous set of PFA when user types n where it is available. 
Type p and press enter where the instructions iclude "type p for previous". This instruction is not visible at the first set of PFAs.
![Previous set of PFA Test](/readme-docs/validate_pfa_choice_press_p.png)
The application will display the previous set of PFAs and await further user input.
If the p is inputed where it was not available, like for the first set of PFA, the input is treated as an error as shown below.
![Previous set of PFA to start Test](/readme-docs/validate_pfa_choice_press_p_to_start.png)
