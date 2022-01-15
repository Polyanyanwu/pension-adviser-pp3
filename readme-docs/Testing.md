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
