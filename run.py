import os
from datetime import date
import gspread
import re
from pprint import pprint
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
                raise ValueError("Invalid option. Please choose only 1 or 2.")
        except ValueError as ve:
            print("Invalid option. Please choose only 1 or 2.")


def login():
    """
    This function is working when the user select the login option
    It take input of account number and ATM pin if its matches login will executed
    """
    while True:
        account_number = input("Enter Your Account Number : ")
        pin = input("Enter Your ATM pin : ")
        try:
            account_numbers = personal_details.col_values(1)
            account_details = personal_details.find(account_number)
            if not account_number in account_numbers:
                raise ValueError("Account number not found.\n")
            account_pin = personal_details.cell(account_details.row, 5).value
            if account_pin != pin:
                raise ValueError("Incorrect PIN.\n")
            os.system('clear')
            print("Login successful.")
            break
        except ValueError as ve:
            print(ve)


def create_account():
    """
    This function is working when the user select the create account option. 
    This function collect all the details of the user to create the account 
    and store it to the stoarge spreadsheet and show back the account number and pin to user.
    """
    print(" TO CREATE ACCOUNT, FILL YOUR DETAILS")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    all_personal_details = personal_details.get_all_values()
    last_row = all_personal_details[-1]
    last_account_number = last_row[0]
    if last_account_number is None:
        account_number = "100001"
    else:
        account_number = int(last_account_number) + 1
    date_of_join = date.today().strftime("%Y-%m-%d")
    while True:
        name = input("\nEnter Name : ")
        if not name.strip() or not all(char.isalpha() or char.isspace() for char in name):
            print("Invalid name. Name cannot be empty and Please enter only alphabets and spaces.")
        else:
            break
    while True:
        address = input("\nEnter Address : ")
        if not address.strip():
            print("Address cannot be empty.\n")
        else:
            break
    while True:
        mobile_number = input("\nEnter Mobile Number : ")
        if not mobile_number.strip() or not mobile_number.isdigit() or len(mobile_number) != 10:
            print("Invalid mobile number. Please enter a 10-digit number.")
        else:
            break
    while True:
        pin_number = input("\nChoose a 4 digit Pin Number for your Account : ")
        if not pin_number.strip() or not pin_number.isdigit() or len(pin_number) != 4:
            print("Invalid PIN number. Please enter a 4-digit number.\n")
        else:
            break
    while True:
        email = input("\nEnter Email: ")
        if not email.strip() or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address.\n")
        else:
            break
    while True:
        print("\nChoose an address proof you have")
        print("1. Valid Passport")
        print("2. Valid Driving Licence")
        print("3. Valid Recidency Permit")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                address_proof_document = "Passport"
                break
            elif option == 2:
                address_proof_document = "Driving Licence"
                break
            elif option == 3:
                address_proof_document = "Recidency Permit"
                break
            else:
                raise ValueError("Invalid option. Please choose only 1,2 or 3.")
        except ValueError as ve:
            print("Invalid option. Please choose only 1,2 or 3.")
    while True:
        document_number = input("\nEnter Document Number: ")
        if not document_number.strip() or not document_number.isdigit() or len(document_number) != 8:
            print("Invalid document number. Please enter an 8-digit number.")
        else:
            break
    row_personal = [account_number, name, address, mobile_number, pin_number, date_of_join, email, address_proof_document, document_number]
    personal_details.append_row(row_personal)
    row_statement = [ account_number, date_of_join, "Initialize", "0", "0", "0" ]
    statement.append_row(row_statement)
    os.system('clear')
    print("Account created successfully.\n")
    print(" ACCOUNT DETAILS")
    print("*-*-*-*-*-*-*-*-*\n")
    print(f"Account Number : {account_number}")
    print(f"ATM Pin : {pin_number}")
    print("\n Save This details for further procedures \n\n")
    while True:
        print("\nDo You want to login Now ? Choose 1 for 'Yes' or 2 for 'No'")
        print("1. Yes")
        print("2. No")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                login()
                break
            elif option == 2:
                os.system('clear')
                main()
                break
            else:
                raise ValueError("Invalid option. Please choose only 1 or 2.")
        except ValueError as ve:
            print("Invalid option. Please choose only 1 or 2.")

main()