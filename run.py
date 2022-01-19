""" controlling module of the application
    calls other modules to execute the
    operations of the application
"""
from pension.intro import introduction, instruction_manager, main_menu
from pension.enquiries import run_enquiry, print_enquiry_result
from pension.model import fetch_existing_results, delete_existing_results

user_name = introduction()
print(f"\n Welcome {user_name}!")

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
        delete_existing_results(user_name)
