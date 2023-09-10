class Bank_Account:
    def __init__(self, account, pin, balance):
        self.account = account
        self.user_pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Amount Deposited: +${amount}')
            return f'Balance: ${self.balance}, Deposit: ${amount}'
        else:
            return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Amount Withdrawn: -${amount}')
            return f'Balance: ${self.balance}, Withdrawn: ${amount}'
        else:
            return "Withdrawal amount is invalid or exceeds your balance."

    def display_transaction_history(self):
        return '\n'.join(self.transaction_history)

    def transfer(self, recipient_account_no, amount):
        if recipient_account_no in account_numbers:
            recipient_index = account_numbers.index(recipient_account_no)
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                balances[recipient_index] += amount
                self.transaction_history.append(f'Amount transferred to ${recipient_account_no}: ${amount}')
                return f'Balance: ${self.balance}'
            else:
                return "Transfer amount is invalid or exceeds your balance."
        else:
            return "Recipient account does not exist."

    def quit(self):
        return "Thank you for using ATM. Have a great day!"

# Initialize an instance of the Bank_Account class
account_numbers = ["363123", "384234", "785567"]
pin_store = [234, 345, 567]
balances = [1000, 2000, 3267]

account_no = input("Enter your acc. no.:")
account_pin = int(input("Enter account pin:"))

# Find the index of the account number in the list
if account_no in account_numbers:
    account_index = account_numbers.index(account_no)
    account = Bank_Account(account_no, account_pin, balances[account_index])
else:
    print("Account not found or incorrect PIN. Please check your account number and PIN.")
    exit()

# Main function to interact with the ATM
def main():
    while True:
        print("\n-----ATM OPERATIONS AVAILABLE------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transaction History")
        print("4. Transfer")
        print("5. Quit")
        choice = int(input("Enter your choice between 1-5:"))
        
        if choice == 1:
            amount = float(input("Enter the amount to be deposited:"))
            print(account.deposit(amount))
        elif choice == 2:
            amount = float(input("Enter the amount to be withdrawn:"))
            print(account.withdraw(amount))
        elif choice == 3:
            print(account.display_transaction_history())
        elif choice == 4:
            recipient_account_no = input("Enter the account no. for money to be transferred:")
            amount = float(input("Enter the amount to be transferred:"))
            print(account.transfer(recipient_account_no, amount))
        elif choice == 5:
            print(account.quit())
            break
        else:
            print("Invalid choice! Select between 1-5.")

if __name__ == "__main__":
    main()
