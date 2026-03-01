import getpass


class BankAccount:

    def __init__(self, pin):
        self.balance = 0
        self.pin = pin

    def authenticate(self):
        entered_pin = getpass.getpass("Enter your PIN: ")
        return entered_pin == self.pin

    def deposit(self):
        if self.authenticate():
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print("Deposit successful, account balance is {self.balance}")
            else:
                print("Amount must be above 0")
        else:
            print("Incorrect PIN")

    def withdraw(self):
        if self.authenticate():
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print("Withdrawal successful")
        else:
            print("Incorrect PIN")

    def check_balance(self):
        if self.authenticate():
            print("Current Balance:", self.balance)
        else:
            print("Incorrect PIN")


# Create account with a PIN
account = BankAccount(pin=getpass.getpass("Set pin: "))

# Menu loop
while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account.deposit()

    elif choice == "2":
        account.withdraw()

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid option. Try again.")