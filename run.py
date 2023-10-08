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

"""
function to achieve type writer effect for texts
credit: Perplexity.AI
"""
import sys
import time

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def main():
    """
    This is the main funtion that initialize the programm
    """
    while True:
        typewriter_effect("\n\n  WELCOME TO ATM")
        typewriter_effect("\n*-*-*-*-*-*-*-*-*\n")
        print("\nChoose from the following options")
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
            after_login(account_number)
            break
        except ValueError as ve:
            print(ve)

def after_login(account_number):
    """
    This function is colled from the login function if the account number and pn matches.
    This Function is the gateway to functions for deposit, withdrowal, balance enquiry and change pin
    """
    account_details = personal_details.find(account_number)
    account_name = personal_details.cell(account_details.row, 2).value
    
    while True:
        typewriter_effect(f"\n\n  HELLO {account_name}")
        typewriter_effect("\n*-*-*-*-*-*-*-*-*\n")
        print("\nChoose from the following options")
        print("\n1. Deposit")
        print("2. Withdrawal")
        print("3. Balance Enquiry")
        print("4. Change Pin Number")
        print("5. Exit")
        option = input("-->> ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                deposit(account_number)
                break
            elif option == 2:
                os.system('clear')
                withdrawal(account_number)
                break
            elif option == 3:
                os.system('clear')
                balance_enquiry(account_number, account_name)
                break
            elif option == 4:
                os.system('clear')
                change_pin(account_number)
                break
            elif option == 5:
                os.system('clear')
                main()
            else:
                raise ValueError("Invalid option. Please choose options from 1 to 5 only.")
        except ValueError as ve:
            print("Invalid option. Please choose options from 1 to 5 only.")


def deposit(account_number):
    """
    This function works for the deposition of money. 
    It collects the number's of deferent notes and calculate the total amount and store the data to the statement
    """
    account_number = account_number
    num_500 = 0
    num_200 = 0
    num_100 = 0
    num_50 = 0
    num_20 = 0
    num_10 = 0
    num_5 = 0
    while True:
        print("Choose the note")
        print("1. 500 euro Notes")
        print("2. 200 euro Notes")
        print("3. 100 euro Notes")
        print("4. 50 euro Notes")
        print("5. 20 euro Notes")
        print("6. 10 euro Notes")
        print("7. 5 euro Notes")
        print("8. Proceed Deposit")
        print("9. Exit")
        option = input("-->> ")
        try:
            option = int(option)
            if option == 1:
                while True:
                    num_500 = input("\nEnter the Number of 500 euro Notes : ")
                    if not num_500.isdigit() and int(num_500)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 2:           
                while True:
                    num_200 = input("\nEnter the Number of 200 euro Notes : ")
                    if not num_200.isdigit() and int(num_200)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 3:
                while True:
                    num_100 = input("\nEnter the Number of 100 euro Notes : ")
                    if not num_100.isdigit() and int(num_100)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 4:
                while True:
                    num_50 = input("\nEnter the Number of 50 euro Notes : ")
                    if not num_50.isdigit() and int(num_50)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 5:   
                while True:
                    num_20 = input("\nEnter the Number of 20 euro Notes : ")
                    if not num_20.isdigit() and int(num_20)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 6:
                while True:
                    num_10 = input("\nEnter the Number of 10 euro Notes : ")
                    if not num_10.isdigit() and int(num_10)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 7:
                while True:
                    num_5 = input("\nEnter the Number of 5 euro Notes : ")
                    if not num_5.isdigit() and int(num_5)< 0:
                        print("Please enter a positive number.")
                    else:
                        break
            elif option == 8: 
                if num_500 == 0 and num_200 == 0 and num_100 ==0 and num_50 == 0 and num_20 == 0 and num_10 == 0 and num_5 == 0:
                    print("\nYou did not choose any note to deposit\n")
                    deposit(account_number)
                else:
                    total_amount = (int(num_500)*500) + (int(num_200)*200) + (int(num_100)*100) + (int(num_50)*50) + (int(num_20)*20) + (int(num_10)* 10) +(int(num_5)*5)
                    while True:
                        os.system('clear')
                        print ("\nConfirm your number of notes")
                        if not num_500 == 0 :
                            print(f"500 x {num_500}")
                        if not num_200 == 0 :
                            print(f"200 x {num_200}")
                        if not num_100 == 0 :
                            print(f"100 x {num_100}")
                        if not num_50 == 0 :
                            print(f"50 x {num_50}")
                        if not num_20 == 0 :
                            print(f"20 x {num_20}")
                        if not num_10 == 0 :
                            print(f"10 x {num_10}")
                        if not num_5 == 0 :
                            print(f"5 x {num_5}")
                        print(f"\nTOTAL AMOUNT : {total_amount}\n")
                        print("\n1. Confirm")
                        print("2. Cancel")
                        option = input("-->> ")
                        try:
                            option = int(option)
                            if option == 1:
                                deposit_date = date.today().strftime("%Y-%m-%d")
                                all_statement = statement.get_all_values()
                                customer_statement = []
                                for row in all_statement:
                                    if row[0] == account_number:
                                        customer_statement.append(row)
                                last_transaction = customer_statement[-1]
                                balance = int(last_transaction[5])
                                balance += total_amount
                                row_statement = [ account_number, deposit_date, "Deposit", "0", total_amount , balance ]
                                statement.append_row(row_statement)
                                typewriter_effect("Transaction is processing... Please wait\n")
                                typewriter_effect("Transaction compleated.\n")
                                print(f"\nAVAILABLE BALANCE : €{balance}")
                                print("\nDo you want to perform another transaction?")
                                print("1. More transaction")
                                print("2. Exit")
                                option = input("-->> : ")
                                try:
                                    option = int(option)
                                    if option == 1:
                                        os.system('clear')
                                        after_login(account_number)
                                        break
                                    elif option == 2:
                                        os.system('clear')
                                        main()
                                        break
                                    else:
                                        raise ValueError("Invalid option. Please choose only 1 or 2.")
                                except ValueError as ve:
                                    print("Invalid option. Please choose only 1 or 2.")
                                break
                            elif option == 2:
                                os.system('clear')
                                main()
                                break
                            else:
                                raise ValueError("Invalid option. Please choose only 1 or 2.")
                        except ValueError as ve:
                            print("Invalid option. Please choose only 1 or 2.")
                break
            elif option ==9:
                main()
            else:
                raise ValueError("Invalid option. Please choose options from 1 to 9 only.")
        except ValueError as ve:
            print("Invalid option. Please choose options from 1 to 9 only.")


def withdrawal(account_number):
    """
    This Function works for the cash withdrowal
    """
    while True:
        print("\nNote: The machine do not give coin.\nEnter an amout multiple of 5 \n")
        withdrow_amount = input("-->> ")
        try:           
            if int(withdrow_amount) % 5 or not withdrow_amount.strip() or not withdrow_amount.isdigit() :
                print("Invalid Amount\n")
            else:
                deposit_date = date.today().strftime("%Y-%m-%d")
                all_statement = statement.get_all_values()
                customer_statement = []
                for row in all_statement:
                    if row[0] == account_number:
                        customer_statement.append(row)
                last_transaction = customer_statement[-1]
                balance = int(last_transaction[5])
                if int(withdrow_amount) > int(balance):
                    os.system('clear')
                    print("Insufficiant balance")
                    print(f"\nAVAILABLE BALANCE : €{balance}")
                    main()
                    break
                else:
                    balance -= int(withdrow_amount)
                    row_statement = [ account_number, deposit_date, "Withdrow", withdrow_amount, "0" , balance ]
                    statement.append_row(row_statement)
                    typewriter_effect("Transaction is processing... Please wait\n")
                    typewriter_effect("Transaction compleated. Collect your cash from the tray\n")
                    print(f"\nAVAILABLE BALANCE : €{balance}")
                    print("\nDo you want to perform another transaction?")
                    print("1. More transaction")
                    print("2. Exit")
                    option = input("-->> : ")
                    try:
                        option = int(option)
                        if option == 1:
                            os.system('clear')
                            after_login(account_number)
                            break
                        elif option == 2:
                            os.system('clear')
                            main()
                            break
                        else:
                            raise ValueError("Invalid option. Please choose only 1 or 2.")
                    except ValueError as ve:
                        print("Invalid option. Please choose only 1 or 2.")
                    break
        except ValueError as ve:
            print("Invalid Amount\n")


def balance_enquiry(account_number, account_name):
    """
    This function is for balance enquery
    """
    all_statement = statement.get_all_values()
    customer_statement = []
    for row in all_statement:
        if row[0] == account_number:
            customer_statement.append(row)
    last_transaction = customer_statement[-1]
    balance = int(last_transaction[5])
    typewriter_effect(f"\nHello {account_name}")
    typewriter_effect(f"\n\nAVAILABLE BALANCE €{balance}\n\n")
    print("\nDo you want to perform another transaction?")
    print("1. More transaction")
    print("2. Exit")
    option = input("-->> : ")
    try:
        option = int(option)
        if option == 1:
            os.system('clear')
            after_login(account_number)
        elif option == 2:
            os.system('clear')
            main()
        else:
            raise ValueError("Invalid option. Please choose only 1 or 2.")
    except ValueError as ve:
        print("Invalid option. Please choose only 1 or 2.")

def change_pin(account_number):
    """
    This function works if the user need to change their ATM pin
    """
    all_personal_details = personal_details.get_all_values()
    personal_detail = []
    for row in all_personal_details:
        if row[0] == account_number:
            personal_detail = row
    new_pin= input("\nEnter new PIN : ")
    while True:
        print("Are you sure you want to change the PIN")
        print("1. Change PIN")
        print("2. Cancel")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                for row in all_personal_details:
                    if row[0] == account_number:
                        row_index = all_personal_details.index(row) + 1
                        personal_details.update_cell(row_index, 5, new_pin)
                typewriter_effect("Updating your ATM PIN... Please wait\n")
                typewriter_effect("Successfully changed your PIN \n")
                typewriter_effect(f"\nNEW PIN : {new_pin}\n")
                print("\nDo you want to perform another transaction?")
                print("1. More transaction")
                print("2. Exit")
                option = input("-->> : ")
                try:
                    option = int(option)
                    if option == 1:
                        os.system('clear')
                        after_login(account_number)
                        break
                    elif option == 2:
                        os.system('clear')
                        main()
                        break
                    else:
                        raise ValueError("Invalid option. Please choose only 1 or 2.")
                except ValueError as ve:
                    print("Invalid option. Please choose only 1 or 2.")
                break
            elif option == 2:
                os.system('clear')
                after_login
            else:
                raise ValueError("Invalid option. Please choose only 1 or 2.")
        except ValueError as ve:
            print("Invalid option. Please choose only 1 or 2.")




def create_account():
    """
    This function is working when the user select the create account option. 
    This function collect all the details of the user to create the account 
    and store it to the stoarge spreadsheet and show back the account number and pin to user.
    """
    typewriter_effect(" FILL OUT THE FOLLOWING DETAILS TO CREATE ACCOUNT\n")
    typewriter_effect("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
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
    typewriter_effect(" ACCOUNT DETAILS\n")
    typewriter_effect("*-*-*-*-*-*-*-*-*\n")
    print(f"Account Number : {account_number}")
    print(f"ATM Pin : {pin_number}")
    print("\n NOTICE: Save This details for further procedures \n\n")
    while True:
        print("\nDo You want to login Now ?")
        print("1. Login")
        print("2. Exit")
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