import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sales_data')

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data of units from the last selling day.")
    print("Data should be 5 numbers, separated by commas")
    print("Example: 1,2,3,4,5\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_sales_data()