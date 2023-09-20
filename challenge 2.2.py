class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ₹ {amount}. New balance: ₹ {self._account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ₹ {amount}. New balance: ₹ {self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name}:   ₹  {self._account_balance}")


# Test the BankAccount class
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder_name, initial_balance)

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == 3:
        account.display_balance()
    elif choice == 4:
        print("Thank you for using the BankAccount program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")