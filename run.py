# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from src.intro import introduction, instruction_manager
from src.utils import confirm_yes_no
from src.enquiries import run_enquiry

user_name = introduction()
print(f"Welcome {user_name}!")
DISPLAY_INSTRUCTION = \
    confirm_yes_no("Would you like to go through the instructions?")
if DISPLAY_INSTRUCTION:
    instruction_manager()
run_enquiry(user_name)
