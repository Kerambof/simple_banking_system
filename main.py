import getpass  # To hide PIN input

class BankAccount:
    def __init__(self, owner, accno, pin):
        self.owner = owner
        self.balance = 0
        self.accno = accno
        self.pin = pin

    def authenticate(self):
        entered_pin = getpass.getpass("Enter your pin: ")  # Hides input securely
        return entered_pin == self.pin

    def deposit(self):
        if self.authenticate():
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposit successful! Your balance is {self.balance}")
            else:
                print("Amount must be positive.")
        else:
            print("Wrong pin, please try again.")

    def check_balance(self):
        if self.authenticate():
            print(f"Your balance is {self.balance}")
        else:
            print("Wrong pin, please try again.")

    def withdraw(self):
        if self.authenticate():
            amount = int(input("Enter amount to withdraw: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"You have successfully withdrawn {amount}. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Wrong pin, please try again.")

    def transfer_money(self, accounts):
        if self.authenticate():
            receiver_acc = input("Enter receiver account number: ")
            if receiver_acc in accounts:
                receiver = accounts[receiver_acc]
                amount = int(input("Enter amount to transfer: "))
                if 0 < amount <= self.balance:
                    self.balance -= amount
                    receiver.balance += amount
                    print(f"Transferred {amount} to {receiver.owner}. Your new balance: {self.balance}")
                else:
                    print("Insufficient balance or invalid amount.")
            else:
                print("Receiver account does not exist.")
        else:
            print("Wrong pin, please try again.")


# Dictionary to store all accounts
accounts = {}


# Function to create a new account
def create_account():
    owner = input("Enter your name to create account: ")
    accno = input("Set account number: ")
    pin = getpass.getpass("Set your pin: ")  # Hide PIN during account creation

    if accno in accounts:
        print("Account number already exists. Choose another one.")
        return

    account = BankAccount(owner, accno, pin)
    accounts[accno] = account
    print(f"Account for {owner} created successfully!")


# Function to select an account
def select_account():
    accno = input("Enter your account number: ")
    if accno in accounts:
        return accounts[accno]
    else:
        print("Account does not exist.")
        return None


# Main menu loop
while True:
    print("\n--- Bank Menu ---")
    print("1: Create new account")
    print("2: Deposit")
    print("3: Check balance")
    print("4: Withdraw")
    print("5: Transfer money")
    print("100: Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice in ["2", "3", "4", "5"]:
        account = select_account()
        if account:
            if choice == "2":
                account.deposit()
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                account.withdraw()
            elif choice == "5":
                account.transfer_money(accounts)
    elif choice == "100":
        print("Thanks for banking with us!")
        break
    else:
        print("Invalid choice. Try again.")