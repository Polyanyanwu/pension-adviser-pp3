""" controlling module of the application
    calls other modules to execute the
    operations of the application
"""
from src.intro import introduction, instruction_manager, main_menu
from src.enquiries import run_enquiry, print_enquiry_result
from src.model import fetch_existing_results

user_name = introduction()
print(f"Welcome {user_name}!")

while True:
    user_action = main_menu()
    if user_action == '9':
        print("\nThank you for consulting the Nigerian Pension Adviser")
        break
    elif user_action == '1':
        instruction_manager()
    elif user_action == '2':
        print_enquiry_result(fetch_existing_results(user_name))
    elif user_action == '3':
        run_enquiry(user_name)
    elif user_action == '4':
        print("delete_exiting_enquiry")
