""" run the enquiries the user wants on the pension returns on investment """

from getch import getch
from pension.model import get_fund_years, fetch_pfas,\
    fetch_return_rates, save_results
from pension.color_prints import print_cyan, print_yellow,\
    print_white, print_red


def _display_fund_choices():
    """ display fund choices to user """
    print_yellow("Great! Let's get started\n")
    print_cyan("Select the Fund of interest by typing", '')
    print_yellow("1, 2, 3, or 4")
    print_yellow("1: ", '')
    print_white("Fund I: Retirement Savings Account(RSA) Fund I")
    print_white("    fund for an Active Contributor", "")
    print_white("who is below 50 yrs of age")
    print_white("    and chooses for contribution to be invested in this fund")
    print_yellow("2: ", '')
    print_white("Fund II: Default fund for all Active Contributors who are")
    print_white("    below 50 yrs of age")
    print_yellow("3: ", '')
    print_white("Fund III: Default fund for all Active Contributors who are")
    print_white("    50 yrs and above")
    print_yellow("4: ", '')
    print_white("Fund IV:  RSA Fund for Retirees only")


def run_enquiry(user: str):

    """ get the Fund type, years and PFA for the enquiry"""

    # get the fund type from user
    fund_type = get_fund_type()

    # get start and end year
    start_end_years = get_years(int(fund_type))

    # get pfa
    pfa_selected = get_pfa()

    result = compute_results(fund_type, start_end_years, pfa_selected)
    print_enquiry_result(result)
    print_yellow("\n Saving enquiry results ...")
    save_results(user.lower(), result)
    return user


def get_fund_type():
    """ prompt the user with available fund types and
    obtain valid selection from user
    Returns:
        the selected fund type
    """
    _display_fund_choices()
    while True:
        print_white("Please enter your choice", '')
        print_yellow("1, 2, 3, or 4 : ", "")
        fund_choice = input("")
        if validate_selection((1, 2, 3, 4), fund_choice):
            if confirm_entry(fund_choice):
                break
            else:
                _display_fund_choices()
    return fund_choice


def validate_selection(choice_tuple: tuple, choice_input):
    """ validate the choice is number contained in the tuple """
    # choices = (1, 2, 3, 4)
    try:
        choice = int(choice_input)
        if choice not in choice_tuple:
            raise ValueError(
                f"Your input must be in {choice_tuple}: you entered {choice}"
            )
    except ValueError as val_error:
        print_red(f"Invalid data: {val_error}, please try again.\n")
        return False
    return True


def confirm_entry(str_entered):
    """ confirm that data entered is same as to be entered """

    print_yellow(f"Confirm your entry by typing {str_entered} again: ", '')
    new_input = input()
    if str(str_entered) != new_input:
        print_red(f"Your entry {str_entered} differs from ", "")
        print_red(f"your confirmation {new_input}")
        print_cyan("Press any Key to try again...")
        getch()
        return False
    return True


def get_years(fund_type: int):
    """
    Get start and end year from user
    Argument:
        fund_type - user selected fund type number
    Return:
        start year and end year from user input
     """
    valid_years = get_fund_years(fund_type)
    if valid_years is None:
        print_red("Could not retrieve valid years ", "")
        print_red("from Google sheet. Try later")
        return None

    while True:
        print()
        print_cyan(f"Valid year range is {valid_years[0]} to {valid_years[1]}")
        start_year = input(" Please enter Start Year: ")
        if validate_year(valid_years, start_year):
            break
    while True:
        print_cyan(f"Valid year range is {valid_years[0]} to {valid_years[1]}")
        end_year = input(" Please enter End Year: ")
        if validate_year(valid_years, end_year):
            if int(start_year) > int(end_year):
                print_red("End Year must be greater or equal to Start Year")
            else:
                break
    return(start_year, end_year)


def validate_year(valid_years, year_to_validate):
    """ validate year entered by user """

    try:
        year_input = int(year_to_validate)
        year_range = range(valid_years[0], valid_years[1]+1, 1)
        if year_input not in year_range:
            raise ValueError(
                "Your input must be in range "
                + f"{valid_years[0]} to {valid_years[1]}"
            )
    except ValueError as val_error:
        print_red(f"Invalid data: {val_error}, please try again.\n")
        return False
    return True


def get_pfa():
    """ display a list of pfas for user to select
    0 will be No PFA
    User must make a selection
    PFAs are displayed in batches
    User can input n for next set or p for previous where necessary

    Returns:
        selected PFA number (0 is for no PFA)
    """
    pfas = fetch_pfas()
    pfa_set = 1
    group_size = 5
    extra_options = ('0')
    pfa_options = tuple(range(pfa_set, pfa_set+5, 1))
    choice = None
    while True:
        print()
        print_cyan("Please select a PFA by typing the number beside the Name")
        # check if to display instruction for next or previous
        if pfa_set == 1:
            print_yellow("Type n to display Next list")
            extra_options = ('0', 'n')
        elif pfa_set * group_size < len(pfas):
            print_yellow("Type n to display Next list or p for Previous")
            extra_options = ('0', 'n', 'p')
        else:
            print_yellow("Type p for Previous")
            extra_options = ('0', 'p')
        print_yellow(0, "")
        print_white("I do not wish to select a PFA")
        for ind in pfa_options:
            print_yellow(ind, "")  # print pfa ID numbers in different color
            # print the pfa name (full name and short name in brackets)
            print_white(f"{pfas[ind-1][2]} ({pfas[ind-1][1]})")
        choice = input("Please enter your choice: ")
        if choice in extra_options \
                or validate_selection((0, ) + pfa_options, choice):
            if choice == 'n':
                pfa_set += 1
                end_range = pfa_set * group_size + 1
                if end_range > len(pfas):
                    end_range = len(pfas) + 1
                pfa_options = \
                    tuple(range((pfa_set - 1) * group_size + 1, end_range, 1))
            elif choice == 'p':
                pfa_set -= 1
                pfa_options = tuple(range((pfa_set - 1)
                                    * group_size + 1, pfa_set
                                    * group_size + 1, 1))
            else:
                if confirm_entry(choice):
                    break
    if int(choice) == 0:
        return None

    return pfas[int(choice)-1]


def get_fund_code(fund_type: int):
    """
    Compute the fund code to be used in querying
    the Google sheet return rates spreadsheet
    Only 4 fund types are available Fund I, Fund II, Fund III & Fund IV
    Returns:
        the fund code in the required string
    """
    if fund_type <= 3:
        fund_code = "Fund " + "I" * fund_type
    else:
        fund_code = "Fund IV"

    return fund_code


def compute_results(fund_type, years: tuple, pfa):
    """ compute the average returns for the given
        fund type, years and pfa
        Arguments:
            fund_type : the fund type selected by user
            years: the start and end year in a tuple
            pfa: the selected PFA
        Returns:
            a dictionary of the computed results
    """
    rates_data = fetch_return_rates()
    fund_code = get_fund_code(int(fund_type))
    results = []
    # compute result for pfa
    if pfa is not None:
        # compute pfa performance for the given
        # period and fund type
        pfa_no = pfa[0]
        avg = compute_pfa_average(pfa_no, years, fund_code, rates_data)
        pfa_result = f"Average for {pfa[1]}, {fund_code} "
        pfa_result += f"{years[0]} to {years[1]}"
        results.append({"details": pfa_result, "result": f"{avg}%"})

    # compute industry average
    filtered_data = list(filter(lambda item: int(item['year'])
                                >= int(years[0]) and int(item['year'])
                                <= int(years[1]) and item['fund'] ==
                                fund_code, rates_data))
    rates = [item['return_rate'] for item in filtered_data]
    avg = round(sum(rates)/len(rates), 2)

    industry_result = f"Industry Average for {fund_code} "
    industry_result += f"{years[0]} to {years[1]}"
    results.append({"details": industry_result, "result": f"{avg}%"})

    best_pfa = determine_best_pfa_returns(years, fund_code, rates_data)
    best_pfa_result = f"Best PFA for {fund_code} {years[0]} to {years[1]}"
    results.append({"details": best_pfa_result,
                    "result": f"{best_pfa[0]} with {best_pfa[1]}% returns"})
    return results


def compute_pfa_average(pfa, years, fund_code, rates_data):
    """ compute the average returns for a pfa and years
    Returns:
        average returns for the given years, fund, and pfa
    """
    filtered_data = list(filter(lambda item: int(item['year'])
                                >= int(years[0]) and int(item['year'])
                                <= int(years[1]) and item['fund'] ==
                                fund_code and int(item['pfa_no']) ==
                                pfa, rates_data))
    rates = [item['return_rate'] for item in filtered_data]
    if len(rates) == 0:
        return 0
    avg = round(sum(rates)/len(rates), 2)
    return avg


def determine_best_pfa_returns(years, fund_code, rates_data):
    """ compute average return for each pfa and given
    fund type and period
    Return:
        the pfa name and average for the best PFA
        that is PFA with the maximum returns
     """
    pfas = fetch_pfas()
    all_pfa_returns = []
    for pfa in pfas:
        avg = compute_pfa_average(pfa[0], years, fund_code, rates_data)
        all_pfa_returns.append((pfa[1], avg))
    best_pfa = max(all_pfa_returns, key=lambda returns: returns[1])
    return best_pfa


def print_enquiry_result(results):
    """ print the enquiry result """

    if len(results) == 0:
        print_red("No existing data to print. Please run some enquiry first\n")
        return
    print("")
    print_cyan("              Enquiry Results")
    print_cyan("              ===============")
    for result in results:
        print_white(f"{result['details']} :", "")
        print_yellow(f"{result['result']}")
    print("")
