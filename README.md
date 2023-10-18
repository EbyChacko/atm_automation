# ATM Automation

The live link can be found here - [ATM Automation](https://atm-automation-56428b57995b.herokuapp.com/)

![ScreenShot](assets/readme_images/main_image_readme.png)

The ATM Automation Project in Python is a testament to the power of automation in simplifying and enhancing the banking experience. It offers users a secure and efficient way to manage their accounts and perform financial transactions, reflecting the continuous evolution of technology in the banking industry. This project showcases the potential for Python to create versatile and user-friendly applications in the field of finance.

(Developer: Eby Chacko)

___

## Introduction

The ATM Automation Project in Python is a robust and user-friendly system designed to automate various functions of an Automated Teller Machine (ATM). This project leverages Python programming to create a virtual ATM system that mimics the functionality of a real-world ATM. It offers a secure and convenient way for users to perform banking transactions, check balances, withdraw cash, and more.

___

## Table of Contents

- [Project Goals](#project-goals)
- [User Experience](#user-experience)
- [Design](#design)
- [Features](#features)
- [Unimplemented Features](#unimplemented-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Clone the Repository Code Locally](#clone-the-repository-code-locally)
- [Credits](#credits)

___

## Project Goals

The goal of the ATM Automation Project is to design, develop, and implement a comprehensive and efficient automated system for Automated Teller Machines (ATMs). This system aims to enhance the user experience, improve operational efficiency, and ensure the security of financial transactions for both customers and the financial institution.

- __User Goals__

  - Transaction Security: Implement robust security measures to safeguard customer data and financial transactions. This includes encryption, user authentication, and monitoring for any suspicious activity.

  - Cash Management: Optimize cash handling within the ATM, ensuring that it is always adequately stocked and balanced.

  - Transaction History: Maintain a transaction history for customers, allowing them to review their recent transactions and account balances.

  - Financial Insights: Users want to gain insights into their financial habits and patterns. They look for reports, charts, and visualizations that provide a clear overview of their income, expenses, and savings over time. These insights help them make more informed financial decisions.

- __Site Owner Goals__

  - User-Friendly Interface: Develop a user-friendly graphical interface that enables customers to easily conduct a wide range of banking transactions, including cash withdrawals, deposits, balance inquiries, fund transfers, and more.
  - Error Handling: Develop a robust error-handling system to address common transaction errors, ensuring a smooth and error-free user experience.
  - Cost Efficiency: Optimize the operational costs associated with ATM maintenance, security, and cash management.

[Back to Table of Contents](#table-of-contents)

___

## User Experience

- __Target Audience__

  - Bank Customers: Individual account holders, both checking and savings account holders and Business account holders.
  - Small Business Owners: Small business owners who use ATMs for various financial transactions like cash deposits and withdrawals.

  The target users of an ATM automation project are diverse, encompassing a broad range of individuals and entities who rely on ATMs for their banking needs, whether it be for routine transactions, financial emergencies, or the sheer convenience of 24/7 access to banking services. The project aims to serve these users efficiently and securely, enhancing their overall banking experience.

- __User Stories__

As a customer approaching an Automated Teller Machine (ATM), the experience is designed to be user-centric, efficient, and secure. 

The user experience at the ATM is designed to be efficient, secure, and hassle-free. Whether you're conducting routine transactions or addressing unexpected financial needs, the ATM's user-friendly interface and thoughtful design aim to provide you with a seamless and satisfying banking experience.

[Back to Table of Contents](#table-of-contents)

___

## Design

- __Design Choices__

As this program was built for the terminal, there wasn't much in terms of design or colour. 

- __Type Writer Effect__

Since this system operates solely within a terminal environment, there are limited opportunities for complex visual design. To enhance the user experience, I've implemented a typewriter effect for text presentation on the screen. This effect is primarily used for headings and important results, ensuring a balance between engaging presentation and efficient use of time.

___

## Flowchart

A well-designed flowchart for an ATM software project helps developers, testers, and stakeholders understand the system's functionality, interactions, and decision points, ensuring the smooth operation of the ATM and a positive user experience. The flowchart is given below.

![Flowchart](assets/readme_images/flow_chart.webp)

[Back to Table of Contents](#table-of-contents)

___

## Features

### Welcome screen
  
- In this ATM machine software project, there is a welcome screen that greets the customer and provides instructions on how to proceed with transactions. The welcome screen typically displays a welcoming message and offers two options: "Login" for existing customers and "Create Account" for new customers

![Welcome Screen/Page](assets/readme_images/welcome_screen.png)   


### Create Account

  If the customer is a new user, they will find the "Create Account" option on the welcome screen. When this option is chosen, the customer is required to provide personal details, including their name, address, mobile number, and email, as part of the account creation process. Additionally, for security purposes, the ATM will collect the address proof.

The ATM system generates a unique account number for the new user, and the customer is given the freedom to choose their own personal identification number (PIN) to facilitate future transactions.

![Create Account](assets/readme_images/create_account.png)

  After the account creation process is successfully completed, the system will display a confirmation message indicating the success of the process. It will also present the system-generated account number and the customer's chosen ATM PIN. Furthermore, the system will provide clear instructions for the customer to save these details for future transactions. This step ensures that the customer has the necessary information to access their account and conduct ATM transactions securely.

  After this message, the system give two options to the customer:

- Login: This option allows the customer to easily access their account and proceed with ATM transactions.
- Exit: If the customer chooses this option, they can exit the system without proceeding further.

These options provide the customer with the flexibility to either log in and use the ATM or exit the system as needed.

![Successful Message](assets/readme_images/successfull_message.png)

### Login

  If the user is an existing customer, they can log in using their account number and PIN, which they already possess. After successfully logging in, they can access and perform various options, including:

![After Login](assets/readme_images/after_login.png)

- Deposit: This option allows the customer to deposit funds into their account. When a customer selects the "Deposit" option, the ATM system initiates a process for cash deposit. Here's how it works:

![Deposit Number Of Notes](assets/readme_images/deposit_num_notes.png)

1. The customer is prompted to enter the number of notes of each denomination they are depositing. The system will ask for the quantity of each note type 
 2. The ATM system calculates the total deposit amount by multiplying the quantity of each note by its denomination and then summing these values. This total amount is displayed for verification.
3. Upon confirmation of the total amount, the system updates the customer's account statement, recording the deposit amount, and date of the transaction.
4. A deposit confirmation is provided to the customer.

This process ensures that the customer's account is accurately credited with the deposited amount, and a record of the transaction is maintained in their account statement for future reference.


If the customer wishes to perform additional transactions after completing a deposit and receiving the confirmation, the system will provide them with the option to do so. Upon choosing to perform more transactions, the system will guide them back to the after-login page, allowing them to access the main menu where they can select and initiate another transaction or take any other desired action, ensuring a seamless and efficient banking experience.

![Deposit Confirmation](assets/readme_images/deposit_confirm.png)

- Withdraw: Customers can withdraw cash from their account. In the "Withdraw" section, the customer is instructed to enter the withdrawal amount in multiples of 5, as the ATM dispenses only notes, not coins. Here's how the process works:

    1. The customer inputs the desired withdrawal amount, ensuring that it is in 
    2. The ATM system checks whether the requested withdrawal amount is less than or equal to the available account balance.
    3. If the withdrawal amount is both in multiples of 5 and within the available balance, the system proceeds with the withdrawal.

        If the withdrawal amount is not in multiples of 5 or exceeds the available balance, the system displays a message: "Insufficient Balance" and shows the current account balance to inform the customer.

        Additionally, it provides the customer with the following options:

        1. Perform Another Transaction
        2. Exit

![Withdrowal](assets/readme_images/withdrowal.png)

- Balance Enquiry: Customers can check the current balance in their account.

    When a customer selects the "Balance Enquiry" option, the ATM system retrieves the data from the database and displays the current account balance on the screen. Additionally, it provides the customer with the following options:
    1. Perform Another Transaction
    2. Exit

![Balance Enquiry](assets/readme_images/balance_enquiry.png)

- Statement: This option provides access to account statements, showing recent transactions and account activity.

    Additionally, it provides the customer with the following options:
    1. Perform Another Transaction
    2. Exit 

![Statement](assets/readme_images/statement.png)
- Change PIN: Customers can change their ATM PIN for security purposes.

    In the "Change PIN" option, the system follows these steps:
    1. The customer inputs their desired new PIN and confirm they need to update the PIN.
    2. The system processes the new PIN entry and updates the customer's stored PIN with the new one.
    3. After the PIN update is successful, the system displays a message confirming the change, such as "PIN Update Successful."
    4. Additionally, as always it provides the customer with the following options, but in this case the options is slightly changed to the following:
        1. Review details
        2. Exit 
        
![Change PIN](assets/readme_images/change_pin.png)

- View Personal Details: This option allows customers to review and verify their personal information on record.

     the "View Personal Details" section, customers can access it from three main sections: the "After Login" page, the "Change PIN" section, and the "Edit Personal Details" section, which is a subsection of the personal details section in the "After Login" page. Here's how it works:

1. Access from the After Login Page:

    When accessing this section from the "After Login" page, the customer can view their personal details. The system retrieves all personal details from the database and displays them on the screen.
    After viewing their details, the system offers two options:
        
    - Edit Personal Details: If the customer wishes to update or modify any personal information, they can choose this option.
    - Exit: If the customer has finished viewing their details and wants to exit, they can select the "Exit" option.

2. Access from the Change PIN Section:

    Customers can access the "View Personal Details" section from the "Change PIN" section, as it is a related section within the ATM interface.
3. Access from the Edit Personal Details Section:

    This section can also be accessed directly from the "Edit Personal Details" subsection within the personal details section of the "After Login" page.

    In all three cases, the "View Personal Details" section provides customers with the ability to review their personal information, with options to edit details or exit the ATM interface as needed.

![Personal Details](assets/readme_images/personal_details.png)

- Update Personal Details :
    
    The option to edit personal details, as a sub-feature of the personal details section, provides customers with the ability to independently update their information. Customers can change their address, mobile number, or update their address proof as needed, enhancing their autonomy and ensuring that their personal information remains accurate and up-to-date. This feature adds convenience and flexibility to the ATM system, allowing customers to manage their account information seamlessly.

![Update Details](assets/readme_images/update_details.png)

[Back to Table of Contents](#table-of-contents)

___

## Unimplemented Features

### __1. bcrypt Module for ATM Pin Encoding__

Since this system is an ATM and primarily deals with cash transactions, security is of paramount importance. To enhance security, I initially attempted to encrypt the ATM PIN using the "bcrypt" module. However, I encountered an error, specifically the "invalid salt" error, despite multiple attempts to resolve it. Consequently, I made the decision to discontinue the use of this encryption method.
    
The encryption process was functioning as intended. However, when verifying the PIN during the login process, an "invalid salt" error is being displayed.

![Invalid Salt Error](assets/readme_images/Error_invalid_salt.png)

### __2. pyttsx3 module for announcements__ 


In the ATM system, it is common for users to receive audible announcements or instructions as they input their selections. I attempted to implement this feature by importing the "pyttsx3" module. However, I encountered errors during the implementation process, and after multiple attempts to resolve them, I decided to discontinue the use of this module.

### __3. Exit after each the transactions__ 

I understand that, traditionally, in an ATM system, it's standard to configure the software to return to the welcome screen after every transaction as a security measure. However, for the sake of user convenience, I've implemented an option that allows users to navigate back to the after-login screen after each transaction, providing a more user-friendly experience.

### __4. OOP concept__ 

I was not initially aware that utilizing object-oriented programming (OOP) concepts was necessary to achieve a distinction grade for this project. Unfortunately, I only realized this when I had already completed my project. However, I acknowledge the importance of using OOP and intend to incorporate it into my next project.

[Back to Table of Contents](#table-of-contents)

___

## __Technologies Used__

The following is a list of the technologies I used on this project.

1. Python:

Python is the primary programming language used to develop the ATM software. It is a versatile language known for its simplicity and readability.

2. HTML:

HTML is utilized for structuring and rendering web pages. It may be employed for creating web-based interfaces or for documentation purposes.

3. JavaScript:

JavaScript is employed to power the Code Institute mock terminal, adding interactivity and functionality to the web-based interface.

4. Google Sheets:

Google Sheets is used as a data storage and management tool. It allows for organized data storage and retrieval, particularly for user accounts and transaction history.

5. Google Cloud:

Google Cloud provides the necessary APIs for various functions within the project.

6. GitHub:

GitHub is a version control platform used to host and manage the project's source code. It facilitates collaboration among team members and enables version tracking and project history.

7. VS Code:

Visual Studio Code serves as the integrated development environment (IDE) for coding and managing the project. It offers a range of developer tools and extensions to aid in code writing and debugging.

8. Git:

Git is a distributed version control system that is employed to manage code changes, track revisions, and collaborate on software development. It works in conjunction with Git repositories on platforms like GitHub.

Each of these technologies plays a specific role in the project's development and execution, contributing to the successful operation of the ATM software system.

[Back to Table of Contents](#table-of-contents)

___

### __Imported Libraries and Packages Used__

- [tabulate](https://pypi.org/project/tabulate/) is used to create structured and visually appealing tables for presenting information, such as statements, in a user-friendly format.
- [os](https://docs.python.org/3/library/os.html)  library is utilized to implement a clear_screen function. This function enhances the user experience by clearing the terminal screen, reducing clutter, and making interactions more straightforward.
- [re](https://docs.python.org/3/library/re.html) library is employed to perform regular expression matching and validation. In this project, it is used to check the input format for dates, ensuring that they adhere to a specific pattern.
- [sys](https://docs.python.org/3/library/sys.html) is used to control the output behavior of the program. Specifically, it is used to print text letter by letter, creating a typewriter-like effect that can enhance user engagement.
- [gspread](https://docs.gspread.org/en/v5.7.0/) facilitates the connection between the program and Google Sheets. It enables reading and updating data on a Google Sheets document, making it an effective tool for managing and syncing data.

[Back to Table of Contents](#table-of-contents)

___

## Testing 

View Testing and Validation [here.](assets/testing.md)


[Back to Table of Contents](#table-of-contents)

___

## Bugs

| **Bug** | **Solution** |
| --- | --- |
| When a customer selects the "Login" option and fails to log in due to an incorrect account number or PIN, they may find themselves stuck because the login function operates in a loop with no clear escape option. | I created a function called "escape" that provides the user with the option to either retry their login, create a new account, or exit the system. |
| When a ValueError occurs in the login function, the error report was previously being displayed from the main function rather than within the login function.  | Improved the error handling in the login page by appropriate 'try' and 'except' blocks. Additionally, I used the else condition within the if-elif statement to provide more accurate error reporting and better manage exceptions within the login process.|
| After implementing "pyttsx3," and deleted the same because of error, I noticed that the requirements.txt file contained unnecessary or unwanted entries, and as a result, the deployed function was encountering errors rather than functioning as expected. | I deleted the existing requirements.txt file and then recreated it again. then by using the command "pip3 freeze > requirements.txt." fixed the issue and ensured a cleaner and more accurate requirements.txt file for the project. |
|If the personal details in the Google Sheet are empty, the system was displaying an error | I fixed the problem by adding a conditional check: 'If the length of the spreadsheet is 0, then the account number should start from 100001.'
| When implementing the "transfer amount" function, I used float values because transfers can involve not only integer values but also decimal values. If the transfer is completed successfully, the balance amount will be represented as a float value. However, when checking the balance or withdrawing money, I used integer values, which led to the error. | I changed the use of integers in the withdrawal and balance enquiry functions to resolve the error. |


### Unfixed Bugs 

As of now, No Unfixed errors.

[Back to Table of Contents](#table-of-contents)

___

## Deployment

### Version Control
The site was created using the Visual Studio code editor and pushed to github to the remote repository ‘ATM- Automation’.

The following git commands were used throughout development to push code to the remote repo:

- git add <file> - This command was used to add the file(s) to the staging area before they are committed.

- git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

- git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

This project uses [Heroku](https://dashboard.heroku.com/apps/atm-automation), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

___

## Clone the Repository Code Locally
- Navigate to the GitHub Repository you want to clone to use locally:
  - Click on the code drop down button
  - Click on HTTPS
  - Copy the repository link to the clipboard
  - Open your IDE of choice (git must be installed for the next steps)
  - Type git clone copied-git-url into the IDE terminal
  - The project will now of been cloned on your local machine for use.

[Back to Table of Contents](#table-of-contents)

___

## Credits 

Here we credit everywhere we have got content for the website and any code that was taken from other sources.

### Code 

- The code for clearing the terminal was got from [stack overflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
- The code for Type writer effect was got from [stack overflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) and perplexity.ai
- The code for connecting to google sheets was got from [code institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/)

### __Design__
- Flowchart was made using [app.diagrams.net](https://app.diagrams.net/)

___

## __Acknowledgements__
I would like to give special thanks to my mentor, [Graeme Taylor](linkedin.com/in/g--taylor) for his guidance during the development of this project.


[Back to Table of Contents](#table-of-contents) 