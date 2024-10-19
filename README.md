# Simple-Bank-Management-System-Using-SQl-and-SQLite3
This is a simple bank management sysem project made my me earlier this year

This Python script implements a basic banking system using SQLite. It allows users to create accounts, manage their balances, apply for loans, and repay loans with interest. The script utilizes various functionalities like database creation, user registration, balance display, deposit, withdrawal, loan management, and updating user details.

Features
1. Database Creation (create_database function)
Functionality: Creates a SQLite database named bank_database.db with two tables: users and loans.

Tables:

users: Stores user information such as serial number, name, city, address, account number, and balance.

loans: Stores loan information, linked to users by account number, including loan amount, period, monthly payment, interest, and remaining installments.

2. Check Registration (check_registration function)
Functionality: Checks if a user with a specific account number is already registered.

Usage: Helps verify user existence before proceeding with other operations.

3. Add User Details (add_db_values function)
Functionality: Allows new users to add their details (name, city, address, and account number) to the users table.

Usage: Registers new users into the system.

4. Display User Details (display function)
Functionality: Fetches and displays all user details from the users table.

Usage: Admin or users can view all registered users' information.

5. Display Balance (display_balance function)
Functionality: Displays the current balance of a user based on the account number.

Usage: Allows users to check their account balance.

6. Options Menu (options function)
Functionality: Provides a menu with various options for users to manage their accounts.

Options:

Deposit Some Money: Deposits a specified amount into the user's account.

Withdraw Some Money: Withdraws a specified amount from the user's account.

Change Added Details: Updates the user's address and account number.

Apply for a Loan: Allows the user to apply for a loan, specifying the amount and period.

Repay Loan with Interest: Allows the user to repay their loan with interest, reducing the remaining installments.

Display Current Balance: Displays the user's current balance.

Exit: Exits the options menu.

7. Deposit Money (deposit function)
Functionality: Adds a specified amount to the user's account balance.

Usage: Allows users to deposit money into their accounts.

8. Withdraw Money (withdraw function)
Functionality: Withdraws a specified amount from the user's account balance, if funds are sufficient.

Usage: Allows users to withdraw money from their accounts.

9. Change User Details (change_details function)
Functionality: Updates the user's address and account number.

Usage: Allows users to update their personal information.

10. Apply for Loan (apply_for_loan function)
Functionality: Allows users to apply for a loan, calculates the monthly payment and interest, and inserts the loan details into the loans table.

Usage: Users can apply for loans and receive information on their monthly payments.

11. Repay Loan (repay_loan function)
Functionality: Allows users to repay their loans by specifying the amount they wish to pay, updating the remaining installments accordingly.

Usage: Users can repay their loans, ensuring payments are tracked and updated in the database.

How to Use
Create the Database: The script starts by creating the database if it doesn't exist.

User Registration: Prompts the user to register if they are new.

Display Users: Displays all user details for verification.

Options Menu: Users can then manage their account using various options provided in the menu.





------------NOTE-------------------------
For debugging purposes, everything you create a database the previous database entries will be listed, think of it as admin mode.
