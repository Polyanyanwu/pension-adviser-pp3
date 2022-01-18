# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from src.intro import introduction, instruction_manager
from src.utils import confirm_yes_no
from src.enquiries import run_enquiry, print_enquiry_result
from src.model import fetch_existing_results

user_name = introduction()
print(f"Welcome {user_name}!")

while True:
    if confirm_yes_no("Would you like to go through the instructions?"):
        instruction_manager()
    run_enquiry(user_name)
    if not confirm_yes_no("Would you like to make another enquiry?"):
        if not confirm_yes_no("Would you like to display all your enquiries?"):
            break
        else:
            print_enquiry_result(fetch_existing_results(user_name))
            break
print("Thank you for consulting the Nigerian Pension Adviser")
