"""
contains functions to use the Google API to read and update 
data from the Google spreadsheet ofr the application
"""
import gspread
from google.oauth2.service_account import Credentials
from src.color_prints import print_yellow, print_red, print_green

# Credit to Code Institute for the approach to use google spreadsheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
try:
    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("pension_rates")

    PFA_RECORDS = SHEET.worksheet("pfa").get_all_records()
    RATES_RECORDS = SHEET.worksheet("rates").get_all_records()
except gspread.exceptions.APIError as api_error:
    print(f"Error accessing Google API: {api_error}, please try later.\n")
except gspread.exceptions.GSpreadException as gsp_error:
    print(f"Error accessing Google sheet: {gsp_error}, please try later.\n")


def get_fund_years(fund_type: int):
    """ Retrieve the start and end years
    for the given fund type.
    Arguments:
        fund_type: the fund code to be retrieved
    Returns:
        a tuple of the start year and end year
        """
    # determine the fund-code by appending I to Fund fund_type times
    # for Fund IV change the code from Fund IIII to Fund IV
    fund_code = "Fund " + "I" * fund_type
    if fund_code == "Fund IIII":
        fund_code = "Fund IV"
    try:
        filter_fund = \
            list(filter(lambda pfa: pfa['fund'] == fund_code, RATES_RECORDS))
        min_year = min(filter_fund, key=lambda x: x['year'])['year']
        max_year = max(filter_fund, key=lambda x: x['year'])['year']
    # NameError is raised if RATES_RECORDS is not defined
    # which is caused by the Google sheet access issues
    except NameError:
        print("Rates record not found, Google sheet not available.\n")
        return None
    except ValueError as val_error:
        print(f"Fund year error: {val_error}, please try again.\n")
        return None
    return (min_year, max_year)


def fetch_pfas():
    """ fetch the list of PFA codes and names from the
        Google sheet. Convert to list of tuples
    Returns:
        List of tuples containing pfa_no, pfa_short_name and pfa_name
    """
    return [tuple(x.values()) for x in PFA_RECORDS]


def fetch_return_rates():
    """ fetch all return data to be analysed
    in the enquiries module
    Returns:
        list of dictionaries containing
        the performance of each PFA for available fund types
        and years
    """
    return RATES_RECORDS


def save_results(user: str, enq_result: dict):
    """
    persist the result of the enquiry to the spreadsheet
    if the worksheet exist, ensure saving only unique enquiries
    Arguments:
        user: the username to be used as worksheet name
        enq_result: the enquiry result dictionary to be saved
    """
    try:
        worksheet = SHEET.worksheet(user)
        # retrieve old data
        existing_data = worksheet.get_all_values()
    except gspread.WorksheetNotFound:
        # create new worksheet if it is not existing
        worksheet = SHEET.add_worksheet(title=user, rows=0, cols=0)
        existing_data = []
    all_data = existing_data
    data_set = set()
    try:
        # add the existing data to a set to aviod saving an enquiry twice
        for ind in range(1, len(existing_data)):
            data_set.add(existing_data[ind][0])  # add only the detail
        # add the new enquiry result to both set and all data
        for item in enq_result:
            data_set.add(item["details"])
            all_data.append(list(item.values()))
        # clear the existing data on the worksheet
        worksheet.clear()
        # write the header row of worksheet
        worksheet.append_row(list(enq_result[0].keys()))
        # iterate through the set and find the related data in all data
        # and save to the excel spreadsheet
        for detail in data_set:
            equiv_data = list(filter(lambda result: result[0]
                                     == detail, all_data))
            worksheet.append_row(list(equiv_data)[0])
        print_green("Successfully saved enquiry results...\n")
    except ValueError as val_error:
        print_red(f"Error while saving enquiry: The error is - {val_error}")
        print_yellow("Please try again \n")


def fetch_existing_results(user):
    """ fetch all existing enquiry results
    Returns:
        list of dictionaries containing
        the existing enquiry results
    """
    existing_data = []
    try:
        worksheet = SHEET.worksheet(user)
        existing_data = worksheet.get_all_records()
    except gspread.WorksheetNotFound:
        pass
    return existing_data


def delete_existing_results(user):
    """ delete all existing enquiry results
    Arguments:
        user - the username to delete the enquiry results
    Returns:
        True if successful or False if not
    """
    try:
        print_yellow("Deleting existing enquiry results ...")
        worksheet = SHEET.worksheet(user)
        worksheet.clear()
        print_green("Successfully deleted existing results...\n")
        return True
    except gspread.WorksheetNotFound:
        print_red("Sorry no data to delete: Please run enquiry first")
    return False


def user_worksheet_exist(user):
    """
        check if a worksheet already exist for the user
        if so, return True, if not return False
    """
    try:
        SHEET.worksheet(user)
    except gspread.WorksheetNotFound:
        return False
    return True
