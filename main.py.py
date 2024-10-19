import sqlite3

def create_database():
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()
    
    # Create the 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            sno INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cityname TEXT NOT NULL,
            address TEXT NOT NULL,
            account_no TEXT UNIQUE NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')

    # Create the 'loans' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            loan_amount REAL NOT NULL,
            loan_period INTEGER NOT NULL,
            monthly_payment REAL NOT NULL,
            monthly_interest REAL NOT NULL,
            remaining_kisht INTEGER DEFAULT loan_period,
            FOREIGN KEY (user_id) REFERENCES users (account_no)
        )
    ''')
    
    connection.commit()


def check_registration(account_no):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE account_no = ?', (account_no,))
    result = cursor.fetchone()

    return result is not None

def add_db_values():
    name = str(input("Full Name Of the Account Holder: "))
    cityname = str(input("City Of Residence: "))
    address = input("Current Residential Address: ")
    account_no = str(input("Enter the Account Number: "))

    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (name, cityname, address, account_no) VALUES (?,?,?,?)',
                   (name, cityname, address, account_no))
    connection.commit()

def display():
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users;')
    rows_users = cursor.fetchall()
    for row in rows_users:
        print(row)

def display_balance(account_no):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT balance FROM users WHERE account_no = ?', (account_no,))
    result = cursor.fetchone()

    if result is not None:
        balance = result[0]
        print(f"Current Balance: ${balance:.2f}")
    else:
        print(f"Account with account number {account_no} not found.")

def options(account_no):
    while True:
        print("\nOptions:")
        print("1. Deposit Some Money")
        print("2. Withdraw Some Money")
        print("3. Change Added Details (Address and Account Number)")
        print("4. Apply for a Loan")
        print("5. Repay Loan with Interest")
        print("6. Display Current Balance")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter the deposit amount: "))
            deposit(account_no, amount)
        elif choice == 2:
            amount = float(input("Enter the withdrawal amount: "))
            withdraw(account_no, amount)
        elif choice == 3:
            new_address = input("Enter the new address: ")
            new_account_no = input("Enter the new account number: ")
            change_details(account_no, new_address, new_account_no)
        elif choice == 4:
            loan_amount = float(input("Enter the loan amount: "))
            loan_period = int(input("Enter the loan period in months: "))
            apply_for_loan(account_no, loan_amount, loan_period)
        elif choice == 5:
            repay_loan(account_no)
        elif choice == 6:
            display_balance(account_no)
        elif choice ==7:
            print("Exiting... ")
            break
        else:
            print("Invalid choice.")

def deposit(account_no, amount):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()
    
    cursor.execute('UPDATE users SET balance = balance + ? WHERE account_no = ?', (amount, account_no))
    connection.commit()
    print(f"Deposit of ${amount} successful.")

def withdraw(account_no, amount):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT balance FROM users WHERE account_no = ?', (account_no,))
    result = cursor.fetchone()

    if result is not None:
        balance = result[0]
        if balance >= amount:
            cursor.execute('UPDATE users SET balance = balance - ? WHERE account_no = ?', (amount, account_no))
            connection.commit()
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds.")
    else:
        print(f"Account with account number {account_no} not found.")

def change_details(account_no, new_address, new_account_no):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE users SET address = ?, account_no = ? WHERE account_no = ?',
                   (new_address, new_account_no, account_no))
    connection.commit()
    print("Details updated successfully.")

def apply_for_loan(account_no, loan_amount, loan_period):
    interest_rate = 0.07  # 7% interest per annum

    total_amount_due = loan_amount * (1 + interest_rate)
    monthly_payment = total_amount_due / loan_period

    monthly_interest = (total_amount_due - loan_amount) / loan_period

    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    # Explicitly set remaining_kisht to loan_period
    remaining_kisht = loan_period

    cursor.execute('INSERT INTO loans (user_id, loan_amount, loan_period, monthly_payment, monthly_interest, remaining_kisht) VALUES (?,?,?,?,?,?)',
                   (account_no, loan_amount, loan_period, monthly_payment, monthly_interest, remaining_kisht))
    connection.commit()

    print(f"Loan of ${loan_amount} approved.")
    print(f"Monthly payment (including interest): ${monthly_payment:.2f}")
    print(f"Total amount due after {loan_period} months: ${total_amount_due:.2f}")

def repay_loan(account_no):
    connection = sqlite3.connect('bank_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id, loan_amount, loan_period, monthly_payment, monthly_interest, remaining_kisht FROM loans WHERE user_id = ? AND remaining_kisht > 0',
                   (account_no,))
    result = cursor.fetchone()

    if result is not None:
        loan_id, loan_amount, loan_period, monthly_payment, monthly_interest, remaining_kisht = result

        while int(remaining_kisht) > 0:
            print(f"\nRemaining Kisht: {remaining_kisht}")
            print(f"Monthly Payment (including interest): ${monthly_payment:.2f}")

            amount_to_pay = float(input("Enter the amount you want to pay for this month: "))

            if amount_to_pay >= monthly_payment:
                remaining_kisht -= 1
                extra_payment = amount_to_pay - monthly_payment

                # Adjust remaining_kisht based on the extra payment and round up
                remaining_kisht -= -(-extra_payment // monthly_payment)

                cursor.execute('UPDATE loans SET remaining_kisht = ? WHERE id = ?', (remaining_kisht, loan_id))
                connection.commit()

                print(f"Payment successful. Remaining Kisht: {remaining_kisht}")

                if remaining_kisht == 0:
                    print("Loan fully repaid.")
                    break
        # Return to the menu after the loop completes
        print("Returning to the menu...")

    else:
        print("No active loans found for the user.")


 
#This Code is Written By Varun Chauhan of Class XII B

# Step 1: Create the database
create_database()

# Step 2: Ask if the user is a new user
new_user = input("Are you a new user? (yes/no): ").lower()

if new_user == "yes":
    # Step 3: Add user details
    add_db_values()
    print("User details added successfully.")

# Step 4: Display user details
display()

# Step 5: Provide options
account_no = input("Enter your account number: ")
options(account_no)
