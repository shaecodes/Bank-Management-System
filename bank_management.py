class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            print(f"Deposited: ${amount}")
            self.display_balance()
        except TypeError as e:
            print(f"Error: {e}")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Withdrawn: ${amount}")
                self.display_balance()
        except TypeError as e:
            print(f"Error: {e}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

    def __str__(self):
        #returns a formatted string that includes the account number, account holder, and balance of the BankAccount object
        name = ' '.join(self.account_holder)
        return f"Account Number: {self.account_number}\nAccount Holder: {name}\nBalance: {self.balance}"

accounts = []
credentials = {
    "user1": "P@ssw0rd1",
    "user2": "S3cr3tP@ss",
    "user3": "C0mpl3xP@55",
    "user4": "P@$$w0rd!",
    "user5": "MyS3cur3P@ss"
}


def create_account():
    while True:
        account_number = input("Please enter your account number: ")
        if len(account_number) != 7:
            print("Invalid Account Number. Please try again.")
        elif any(account.account_number == account_number for account in accounts):
            print("The provided account number is already associated with an existing account.")
        else:
            break

    while True:
        name = input("Enter the account holder's name (e.g. John Brown): ")
        account_holder = name.split(" ")
        if len(account_holder) != 2:
            print("Invalid name. Enter first and last name. Please try again.")
        else:
            break

    account = BankAccount(account_number, account_holder, balance=0)
    accounts.append(account)


def view_accounts(accounts):
    while True:
        if not accounts:
            print("No account records found.")
        else:
            print("List of Accounts: \n")
            # Using print() function, the __str__ method will be automatically be called, and it will return the string representation of the BankAccount objects in accounts.
            for account in accounts:
                print(account)
                print("")
            break

def run():
    while True:
        print("\nBank Account Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Close Account")
        print("5. View Accounts")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            if not accounts: #checks if the accounts list is empty
                print("No accounts found.")
            else:
                account_number = input("Enter the account number to deposit: ")
                amount = float(input("Enter the amount to deposit: "))
                for account in accounts:
                    if account.account_number == account_number: #checks to see if the account numbers exists
                        account.deposit(amount)
                        break
                else:
                    print("Account not found.")
        elif choice == '3':
            if not accounts:
                print("No accounts found.")
            else:
                account_number = input("Enter the account number to withdraw: ")
                amount = float(input("Enter the amount to withdraw: "))
                for account in accounts:
                    if account.account_number == account_number:
                        account.withdraw(amount)
                        break
                else:
                    print("Account not found.")
        elif choice == '4':
            if not accounts:
                print("No accounts found.")
            else:
                account_number = input("Enter the account number to close: ")
                for account in accounts:
                    if account.account_number == account_number:
                        answer = input("Are you sure you want to close your account? Please enter 'N' for NO: ")

                        if answer.lower()=="n":
                            print("Operation Cancelled. Account not closed")
                        else:
                            print("Account has been closed permanently. Sorry you had to go")
                            accounts.remove(account)
                            break
                else:
                    print("Account not found.")
        elif choice == '5':
            print("Accessing Account Records")
            print("Please enter username and password")
            username = input("> Username: ")
            password = input("> Password: ")

            if username in credentials and credentials[username] == password:
                print("Access granted!")
                view_accounts(accounts)
                break
            else:
                print("Invalid username or password. Access denied.")
        
        elif choice == '6':
            print("Exiting...")
            print("Thank you for using the Bank Account Management System!")
            break
        else:
            print("Error: Invalid choice. Please try again.")


run()
