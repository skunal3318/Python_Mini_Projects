# Basic ATM interface using OOP, Constructor, Conditionals, Loops

class BankAccount:
    def __init__(self, username, pin, balance=0):
        self.username = username
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} debited. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

# Dictionary to store users
my_bank = {}

def register():
    print("\n--- Account Registration ---")
    username = input("Set a username: ")
    if username in my_bank:
        print("Username already exists. Try logging in.")
        return

    try:
        pin = int(input("Set a 4-digit PIN: "))
        amount = float(input("Initial deposit amount: ₹"))
        my_bank[username] = BankAccount(username, pin, amount)
        print("Account created successfully!\n")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def login():
    print("\n--- Account Login ---")
    username = input("Enter your username: ")
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("PIN must be a number.")
        return None

    account = my_bank.get(username)
    if account and account.pin == pin:
        print("Login successful!\n")
        return account
    else:
        print("Incorrect username or PIN.")
        return None

def delete_account():
    print("\n--- Delete Account ---")
    username = input("Enter your username: ")
    try:
        pin = int(input("Enter your PIN to confirm deletion: "))
    except ValueError:
        print("Invalid PIN.")
        return

    account = my_bank.get(username)
    if account and account.pin == pin:
        del my_bank[username]
        print("Account deleted successfully.")
    else:
        print("Incorrect credentials.")

def transactions(account):
    while True:
        print("""
--- Transaction Menu ---
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Back to Main Menu
5. Exit
        """)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 1:
            account.check_balance()
        elif choice == 2:
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == 3:
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == 4:
            break
        elif choice == 5:
            print("Exiting application.")
            exit()
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("""
======= Welcome to MyBank =======
1. Register
2. Login
3. Delete Account
4. Exit
        """)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            register()
        elif choice == 2:
            account = login()
            if account:
                transactions(account)
        elif choice == 3:
            delete_account()
        elif choice == 4:
            print("Thank you for using MyBank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
