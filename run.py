import os
from datetime import date
import gspread
import re
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import sys
import time

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


def typewriter_effect(text):
    """
    function to achieve type writer effect for texts
    credit: Perplexity.AI
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def main():
    """
    This is the main funtion that initialize the programm
    """
    while True:
        typewriter_effect("\n  WELCOME TO ATM")
        typewriter_effect("\n *-*-*-*-*-*-*-*-*\n")
        print("\n Choose from the following options")
        print(" 1.Login")
        print(" 2.Create Account")
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
        except ValueError:
            main()


def login():
    """
    This function is working when the user select the login option
    It take input of account number and ATM pin if its matches
    login will executed
    """
    while True:
        account_number = input("\n\n Enter Your Account Number : ")
        pin = input(" Enter Your ATM pin : ")
        try:
            account_numbers = personal_details.col_values(1)
            account_details = personal_details.find(account_number)
            if account_number not in account_numbers:
                raise ValueError("\n Account number not found.\n")
            account_pin = personal_details.cell(account_details.row, 5).value
            if account_pin != pin:
                raise ValueError("\n Incorrect PIN.\n")
            os.system('clear')
            after_login(account_number)
            break
        except ValueError as ve:
            print(ve)
            login_escape()


def login_escape():
    """
    this function is used when there is an unexpecter error
    occures when login. In this function there are three options.
    try again, create account and exit.
    """
    while True:
        print("1. Try Again")
        print("2. Create Account")
        print("3. Exit")
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
            elif option == 3:
                os.system('clear')
                main()
                break
            else:
                print("Invalid option. Please choose only 1 to 3.")
        except ValueError as ve:
            print(" \nInvalid option. Please choose only 1 to 3.")


def after_login(account_number):
    """
    This function is colled from the login function
    only if the account number and pin matches.
    This Function is the gateway to functions for
    deposit, withdrowal, balance enquiry and change pin
    """
    account_details = personal_details.find(account_number)
    account_name = personal_details.cell(account_details.row, 2).value
    while True:
        typewriter_effect(f"\n  HELLO {account_name}")
        typewriter_effect("\n  *-*-*-*-*-*-*-*-*-*-*-*\n")
        print("\n Choose from the following options")
        print("\n 1. Deposit")
        print(" 2. Withdrawal")
        print(" 3. Balance Enquiry")
        print(" 4. Show Statement")
        print(" 5. Change Pin Number")
        print(" 6. Personal Details")
        print(" 7. Transfer Amount")
        print(" 8. Exit")
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
                account_statement(account_number)
                break
            elif option == 5:
                os.system('clear')
                change_details(account_number, "ATM-PIN")
                break
            elif option == 6:
                os.system('clear')
                show_personal_details(account_number)
                break
            elif option == 7:
                os.system('clear')
                transfer_amount(account_number)
                break
            elif option == 8:
                os.system('clear')
                main()
            else:
                os.system('clear')
                print("\n Invalid option. Choose options from 1 to 7 only.")
        except ValueError as ve:
            os.system('clear')
            print("\n Invalid option. Choose options from 1 to 7 only.")


def number_of_notes(note):
    """
    this function used to input number of notes from the user
    """
    while True:
        num = input(f"\n Enter the Number of {note} euro Notes : ")
        if num.isdigit() and int(num) > 0:
            return num
        else:
            os.system('clear')
            print("\n Please enter a positive number.")


def deposit(account_number):
    """
    This function works for the deposition of money.
    It collects the number's of deferent notes and
    calculate the total amount and store the data to the statement
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
        print("\n\n Choose the note")
        print(" 1. 500 euro Notes")
        print(" 2. 200 euro Notes")
        print(" 3. 100 euro Notes")
        print(" 4. 50 euro Notes")
        print(" 5. 20 euro Notes")
        print(" 6. 10 euro Notes")
        print(" 7. 5 euro Notes")
        print(" 8. Proceed Deposit")
        print(" 9. Cancel")
        print(" 10. Exit")
        option = input("-->> ")
        try:
            option = int(option)
            if option == 1:
                num_500 = number_of_notes("500")
            elif option == 2:
                num_200 = number_of_notes("200")
            elif option == 3:
                num_100 = number_of_notes("100")
            elif option == 4:
                num_50 = number_of_notes("50")
            elif option == 5:
                num_20 = number_of_notes("20")
            elif option == 6:
                num_10 = number_of_notes("10")
            elif option == 7:
                num_5 = number_of_notes("5")
            elif option == 8:
                num_list = [num_500, num_200, num_100,
                            num_50, num_20, num_10, num_5]
                note_list = [500, 200, 100, 50, 20, 10, 5]
                total_amount = calc_amount(num_list, note_list)
                if total_amount == 0:
                    print("\n You did not choose any note to deposit\n")
                    deposit(account_number)
                else:
                    while True:
                        os.system('clear')
                        print("\n Confirm your number of notes")
                        if not num_500 == 0:
                            print(f" 500 x {num_500}")
                        if not num_200 == 0:
                            print(f" 200 x {num_200}")
                        if not num_100 == 0:
                            print(f" 100 x {num_100}")
                        if not num_50 == 0:
                            print(f" 50 x {num_50}")
                        if not num_20 == 0:
                            print(f" 20 x {num_20}")
                        if not num_10 == 0:
                            print(f" 10 x {num_10}")
                        if not num_5 == 0:
                            print(f" 5 x {num_5}")
                        print(f"\nTOTAL AMOUNT : {total_amount}\n")
                        confirm_or_re_enter(account_number, total_amount)
                break
            elif option == 9:
                os.system('clear')
                after_login(account_number)
            elif option == 10:
                os.system('clear')
                main()
            else:
                os.system('clear')
                print("\n Invalid option. Choose options from 1 to 10 only.")
        except ValueError as ve:
            os.system('clear')
            print("\n Invalid option. Choose options from 1 to 10 only.")


def calc_amount(num_list, note_list):
    """
    this function calculate the total amount
    using the number of notes that enter by the user
    """
    return sum([int(num) * note for num, note in zip(num_list, note_list)])


def confirm_or_re_enter(account_number, total_amount):
    """
    This function is working after the user enter all the number of notes
    to confirm the number of notes are correct
    """
    while True:
        print("\n 1. Confirm")
        print(" 2. Re-Enter number of notes")
        option = input("-->> ")
        try:
            option = int(option)
            if option == 1:
                perform_deposit(account_number, total_amount)
                perform_another_transaction(account_number)
                break
            elif option == 2:
                os.system('clear')
                deposit(account_number)
                break
            else:
                print("\n Invalid option. Choose only 1 or 2.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1 or 2.")


def perform_deposit(account_number, total_amount):
    """
    this function is called from the deposit function to perform the deposit
    This function store datas to the spreadsheet.
    """
    deposit_date = date.today().strftime("%Y-%m-%d")
    all_statement = statement.get_all_values()
    customer_statement = []
    for row in all_statement:
        if row[0] == account_number:
            customer_statement.append(row)
    last_transaction = customer_statement[-1]
    balance = int(last_transaction[5])
    balance += total_amount
    row_statement = [account_number, deposit_date, "Deposit", "0",
                     total_amount, balance]
    statement.append_row(row_statement)
    os.system('clear')
    typewriter_effect("Transaction is processing... Please wait\n")
    typewriter_effect("Transaction compleated.\n")
    print(f"\n AVAILABLE BALANCE : €{balance}")


def withdrawal(account_number):
    """
    This Function works for the cash withdrowal
    """
    while True:
        print("\n Note: The machine do not give coin.")
        print(" Enter an amount multiple of 5 \n")
        withdraw_amount = input("-->> ")
        try:
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount % 5 != 0 or \
                    not withdraw_amount != 0:
                print("\n Invalid Amount\n")
            else:
                withdraw_amount = round(withdraw_amount)
                deposit_date = date.today().strftime("%Y-%m-%d")
                all_statement = statement.get_all_values()
                customer_statement = []
                for row in all_statement:
                    if row[0] == account_number:
                        customer_statement.append(row)
                last_transaction = customer_statement[-1]
                balance = float(last_transaction[5])
                if withdraw_amount > balance:
                    os.system('clear')
                    print("\n\n\n Insufficient balance")
                    print(f"\nAVAILABLE BALANCE : €{balance}")
                    main()
                    break
                else:
                    balance -= withdraw_amount
                    row_statement = [account_number, deposit_date,
                                     "Withdraw", withdraw_amount, "0", balance]
                    statement.append_row(row_statement)
                    os.system('clear')
                    typewriter_effect("Transaction is processing... ")
                    typewriter_effect("Please wait\n")
                    typewriter_effect("Transaction completed. ")
                    typewriter_effect("Collect your cash from the tray\n")
                    print(f"\nAVAILABLE BALANCE : €{balance}")
                    perform_another_transaction(account_number)
                    break
        except ValueError as ve:
            os.system('clear')
            print(" Invalid Amount")


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
    balance = float(last_transaction[5])
    typewriter_effect(f"\nHello {account_name}")
    typewriter_effect(f"\n\nAVAILABLE BALANCE €{balance}\n\n")
    perform_another_transaction(account_number)


def change_details(account_number, detail):
    """
    This function works if the user need to
    change their personal details or atm Pin
    """
    all_personal_details = personal_details.get_all_values()
    for row in all_personal_details:
        if row[0] == account_number:
            row_index = all_personal_details.index(row) + 1
            column_index = 0
            if detail == "ATM-PIN":
                new_detail = input_pin()
                column_index = 5
            elif detail == "Name":
                new_detail = input_name()
                column_index = 2
            elif detail == "Address":
                new_detail = input_address()
                column_index = 3
            elif detail == "Mobile Number":
                new_detail = input_Mobile_number()
                column_index = 4
            elif detail == "Email":
                new_detail = input_email()
                column_index = 7
            elif detail == "Address Proof":
                address_proof = input_address_proof()
                document_number = input_document_number()
            while True:
                print(f"\n Are you sure you want to change {detail}")
                print(f" 1. Change {detail}")
                print(" 2. Cancel")
                option = input("-->> : ")
                try:
                    option = int(option)
                    if option == 1:
                        if detail == "Address Proof":
                            personal_details.update_cell(row_index, 8,
                                                         address_proof)
                            personal_details.update_cell(row_index, 9,
                                                         document_number)
                        else:
                            personal_details.update_cell(row_index,
                                                         column_index,
                                                         new_detail)
                        os.system('clear')
                        typewriter_effect(f" Updating your {detail}...")
                        typewriter_effect(f" Please wait\n")
                        typewriter_effect(f" Updation Successfull\n")
                        review_detail(account_number)
                    elif option == 2:
                        os.system('clear')
                        after_login(account_number)
                    else:
                        raise ValueError("Invalid option. Choose only 1 or 2.")
                except ValueError as ve:
                    print("Invalid option. Choose only 1 or 2.")


def input_pin():
    """
    accept user input fot ATM pin and validate it
    """
    while True:
        pin = input("\n Choose a 4 digit Pin Number : ")
        if not pin.strip() or not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN number. Enter a 4-digit number.\n")
        else:
            return pin


def input_name():
    """
    accept user input fot Name and validate it
    """
    while True:
        name = input("\n Enter Name : ")
        if not name.strip() or \
                not all(char.isalpha() or char.isspace() for char in name):
            print("\n Name cannot be empty & Enter only alphabets and spaces.")
        else:
            return name.upper()


def input_address():
    """
    accept user input fot Address and validate it
    """
    while True:
        address = input("\n Enter Address : ")
        if not address.strip():
            print("\n Address cannot be empty.\n")
        else:
            return address


def input_Mobile_number():
    """
    accept user input fot Mobile number and validate it
    """
    while True:
        mobile_number = input("\n Enter Mobile Number : ")
        if not mobile_number.strip() or \
            not mobile_number.isdigit() or \
                len(mobile_number) != 10:
            print("\n Invalid mobile number. Enter a 10-digit number.")
        else:
            return mobile_number


def input_email():
    """
    accept user input fot email and validate it
    """
    while True:
        email = input("\n Enter Email: ")
        if not email.strip() or \
                not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("\n Invalid email address.\n")
        else:
            return email


def input_address_proof():
    """
    accept user input fot address proof and validate it
    """
    while True:
        print("\n Choose an address proof you have")
        print(" 1. Valid Passport")
        print(" 2. Valid Driving Licence")
        print(" 3. Valid Recidency Permit")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                return "Passport"
            elif option == 2:
                return "Driving Licence"
            elif option == 3:
                return "Recidency Permit"
            else:
                raise ValueError("\n Invalid option. Choose only 1,2 or 3.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1,2 or 3.")


def input_document_number():
    """
    accept user input fot Address proof number and validate it
    """
    while True:
        document_number = input("\n Enter Document Number: ")
        if not document_number.strip() or \
            not document_number.isdigit() or \
                len(document_number) != 8:
            print("\n Invalid document number. Enter an 8-digit number.")
        else:
            return document_number


def input_account_number():
    """
    accept user input for Account Number and validate it
    """
    while True:
        receiver = input("\nEnter Account Number of the Receiver: ")
        if not receiver.strip() or not receiver.isdigit():
            os.system('clear')
            print("\n\nInvalid input. Please enter a valid account number.")
            continue
        receiver_details = personal_details.find(receiver)
        if not receiver_details:
            os.system('clear')
            print("\nAccount Number Not Found. Enter a valid account number.")
            continue
        valid_receiver = personal_details.cell(receiver_details.row, 1).value
        if receiver != valid_receiver:
            os.system('clear')
            print("\nAccount Number Not Found. Enter a valid account number.")
            continue
        return receiver


def input_amount():
    while True:
        try:
            amount = float(input("Enter an amount: "))
            if amount <= 0:
                print("Amount must be positive. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return amount


def transfer_amount(account_number):
    reciever = input_account_number()
    transfer_amount = input_amount()
    reciever_details = personal_details.find(reciever)
    reciever_name = personal_details.cell(reciever_details.row, 2).value
    while True:
        print(f" Are You sending Money to {reciever_name} ?")
        print(" 1. Yes")
        print(" 2. No")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                perform_transfer(account_number, reciever,
                                 reciever_name, transfer_amount)
                break
            elif option == 2:
                os.system('clear')
                main()
                break
            else:
                print("\n Invalid option. Choose only 1 or 2.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1 or 2.")


def perform_transfer(account_number, reciever, reciever_name, transfer_amount):
    transaction_date = date.today().strftime("%Y-%m-%d")
    all_statement = statement.get_all_values()
    sender_statement = []
    reciever_statement = []
    for row in all_statement:
        if row[0] == account_number:
            sender_statement.append(row)
        elif row[0] == reciever:
            reciever_statement.append(row)
    last_sender_transaction = sender_statement[-1]
    sender_balance = float(last_sender_transaction[5])
    last_sreciever_transaction = reciever_statement[-1]
    reciever_balance = float(last_sreciever_transaction[5])
    if float(transfer_amount) > float(sender_balance):
        os.system('clear')
        print("\n\n\n Insufficiant balance")
        print(f"\nAVAILABLE BALANCE : €{sender_balance}")
        main()
    else:
        sender_balance -= float(transfer_amount)
        reciever_balance += float(transfer_amount)
        row_sender_statement = [account_number, transaction_date,
                                "Transfer", transfer_amount,
                                "0", sender_balance]
        row_reciever_statement = [reciever, transaction_date,
                                  "Transfer", "0",
                                  transfer_amount, reciever_balance]
        statement.append_row(row_sender_statement)
        statement.append_row(row_reciever_statement)
        os.system('clear')
        typewriter_effect("Transaction is processing... ")
        typewriter_effect("Please wait\n")
        typewriter_effect(f"€{transfer_amount} transferd to {reciever_name} ")
        print(f"\nAVAILABLE BALANCE : €{sender_balance}")
        perform_another_transaction(account_number)


def review_detail(account_number):
    """
    give the customer a option to review the personal details
    """
    while True:
        print("\n Do you want to Review your personal details?")
        print(" 1. Review Details")
        print(" 2. Cancel")
        print(" 3. Exit")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                show_personal_details(account_number)
                break
            elif option == 2:
                os.system('clear')
                after_login(account_number)
                break
            elif option == 3:
                os.system('clear')
                main()
                break
            else:
                raise ValueError("\n Invalid option. Choose only 1,2 or 3.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1,2 or 3.")


def create_account():
    """
    This function is working when the user select the create account option.
    This function collect all the details of the user to create the account
    and store it to the stoarge spreadsheet and
    show back the account number and pin to user.
    """
    typewriter_effect(" FILL OUT THE DETAILS\n")
    typewriter_effect(" *-*-*-*-*-*-*-*-*-*-*-*\n")
    all_personal_details = personal_details.get_all_values()
    length = len(all_personal_details)
    if length == 0:
        heading_statement = ["Account Number", "Name", "Address",
                             "Mobile Number",
                             "Pin Number", "Date of Join", "Email",
                             "Address Proof Document", "Document Number"]
        personal_details.append_row(heading_statement)
        account_number = "100001"
    elif length == 1:
        account_number = "100001"
    else:
        last_row = all_personal_details[-1]
        last_account_number = last_row[0]
        account_number = int(last_account_number) + 1
    date_of_join = date.today().strftime("%Y-%m-%d")
    name = input_name()
    address = input_address()
    mobile_number = input_Mobile_number()
    email = input_email()
    pin_number = input_pin()
    address_proof_document = input_address_proof()
    document_number = input_document_number()
    row_personal = [account_number, name, address, mobile_number, pin_number,
                    date_of_join, email, address_proof_document,
                    document_number]
    personal_details.append_row(row_personal)
    row_statement = [account_number, date_of_join, "Initialize", "0", "0", "0"]
    statement.append_row(row_statement)
    os.system('clear')
    print("\n\n Account created successfully.\n")
    typewriter_effect(" ACCOUNT DETAILS\n")
    typewriter_effect(" *-*-*-*-*-*-*-*-*\n")
    print(f" Account Number : {account_number}")
    print(f" ATM Pin : {pin_number}")
    print("\n NOTICE: Save This details for further procedures \n\n")
    while True:
        print("\n Do You want to login Now ?")
        print(" 1. Login")
        print(" 2. Exit")
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
                print("\n Invalid option. Choose only 1 or 2.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1 or 2.")


def account_statement(account_number):
    """
    for showing the table data of the account statement
    """
    all_statement = statement.get_all_values()
    customer_statement = []
    headers = [""]
    for row in all_statement:
        if row[0] == account_number:
            customer_statement.append(row)
    headers = ["Account Number", "Date", "Transaction", "Debit",
               "credit", "balance"]
    print(tabulate(customer_statement, headers=headers))
    perform_another_transaction(account_number)


def perform_another_transaction(account_number):
    """
    give option to do more transaction from the
    current page to the after login page
    """
    while True:
        print("\n Do you want to perform another transaction?")
        print(" 1. More transaction")
        print(" 2. Exit")
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
                print("\n Invalid option. Choose only 1 or 2.")
        except ValueError as ve:
            print("\n Invalid option. Choose only 1 or 2.")


def show_personal_details(account_number):
    """
    To print all the personal details of the user
    after that gives a chance to edit the details that shown
    """
    all_personal_details = personal_details.get_all_values()
    personal_detail = []
    for row in all_personal_details:
        if row[0] == account_number:
            personal_detail = row
    os.system('clear')
    typewriter_effect("\n\n YOUR PERSONAL DETAILS\n")
    typewriter_effect(" *-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print(f"\n Account Number       : {personal_detail[0]}")
    print(f"\n ATM Pin              : {personal_detail[4]}")
    print(f"\n Name                 : {personal_detail[1]}")
    print(f"\n Address              : {personal_detail[2]}")
    print(f"\n Mobile Number        : {personal_detail[3]}")
    print(f"\n Email                : {personal_detail[6]}")
    print(f"\n Date of Join         : {personal_detail[5]}")
    print(f"\n address proof        : {personal_detail[7]}")
    print(f"\n Address proof Number : {personal_detail[8]}\n")
    while True:
        print("\n Do you want to edit the details")
        print(" 1. Edit")
        print(" 2. Cancel")
        print(" 3. Exit")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                os.system('clear')
                typewriter_effect("\n\n UPDATE YOUR PERSONAL DETAILS\n")
                typewriter_effect(" *-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                call_update_details(account_number)
                break
            elif option == 2:
                os.system('clear')
                after_login(account_number)
                break
            elif option == 3:
                os.system('clear')
                main()
                break
            else:
                print("Invalid option. Choose only 1, 2 or 3")
        except ValueError as ve:
            print("Invalid option. Choose only 1, 2 or 3")


def call_update_details(account_number):
    """
    To edit the personal details of the user as per request
    """
    while True:
        print("\n What you want to change?")
        print(" 1. Name")
        print(" 2. Address")
        print(" 3. Mobile Number")
        print(" 4. Email")
        print(" 5. address proof")
        print(" 6. Cancel")
        option = input("-->> : ")
        try:
            option = int(option)
            if option == 1:
                change_details(account_number, "Name")
            elif option == 2:
                change_details(account_number, "Address")
            elif option == 3:
                change_details(account_number, "Mobile Number")
            elif option == 4:
                change_details(account_number, "Email")
            elif option == 5:
                change_details(account_number, "Address Proof")
            elif option == 6:
                os.system('clear')
                after_login(account_number)
            else:
                print("Invalid option. Choose only from 1 to 6.")
        except ValueError as ve:
            print("Invalid option. Choose only from 1 to 6.")


if __name__ == "__main__":
    main()
