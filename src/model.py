"""
contains functions to use the Google API to read and update 
data from the Google spreadsheet ofr the application
"""
import gspread
from google.oauth2.service_account import Credentials

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
