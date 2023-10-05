import os
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
SHEET = GSPREAD_CLIENT.open('atm-automation')
personal_details = SHEET.worksheet('personal_details')
statement = SHEET.worksheet('statement')

def main():
    """
    This is the main funtion that initialize the programm
    """
    while True:
        status = True
        print("\n\n  WELCOME TO ATM")
        print("*-*-*-*-*-*-*-*-*\n")
        print("Choose from the following options")
        print("1.Login")
        print("2.Create Account")
        option = input("-->> ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                login()
                break
            elif option == 2:
                os.system('clear')
                create_account()
                break
            else:
                raise ValueError("")
        except ValueError as ve:
            os.system('clear')
            print("Invalid option. Please choose only 1 or 2.")
def login():
    print("login")
def create_account():
    print("Create account")
main()