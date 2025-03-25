

#         class
# to work on  
#                 class 
#   this is chat G P T version
# Define the BankAccount class to handle account operations
class BankAccount:
    # Initialize the account with account number and an optional initial balance
    def _init_(self, acc_num, initial_balance=0):
        self.acc_num = acc_num
        self.balance = initial_balance  # Store the account's initial balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount  # Add the deposit amount to the balance
        return self.balance  # Return the updated balance

    # Method to withdraw money from the account
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Subtract the withdrawal amount from the balance
            return self.balance  # Return the updated balance
        else:
            return "Insufficient funds"  # Return an error message if balance is insufficient

    # Method to check the account's current balance
    def check_balance(self):
        return self.balance  # Return the current balance

# Dictionary to store accounts using account numbers as keys
accounts = {}

# Main program loop
while True:
    print('''
1. CREATE ACCOUNT
2. DEPOSIT
3. WITHDRAW
4. CHECK BALANCE
5. EXIT      
    ''')

    # Prompt the user for their choice
    choice = input("Pick an option:\n").strip()

    if choice == '1':
        # Create a new account
        acc_num = input("Enter account number sent to your email:\n").strip()
        initial_balance = float(input("Enter initial balance:\n"))
        accounts[acc_num] =  BankAccount(acc_num, initial_balance)  # Create and store a new BankAccount
        print("ACCOUNT CREATED.")

    elif choice == '2':
        # Deposit money into an account
        acc_num = input("Enter account number:\n").strip()
        if acc_num in accounts:
            dep_amount = float(input("Enter deposit amount:\n"))
            new_bal = accounts[acc_num].deposit(dep_amount)
            print("New balance is:", new_bal)
        else:
            print("Invalid account number:", acc_num)

    elif choice == '3':
        # Withdraw money from an account
        acc_num = input("Enter account number:\n").strip()
        if acc_num in accounts:
            withdraw_amount = float(input("Enter withdrawal amount:\n"))
            result = accounts[acc_num].withdrawal(withdraw_amount)
            if isinstance(result, str):
                print(result)  # Print error message if funds are insufficient
            else:
                print("New balance is:", result)
        else:
            print("Invalid account number:", acc_num)

    elif choice == '4':
        # Check the balance of an account
        acc_num = input("Enter account number:\n").strip()
        if acc_num in accounts:
            bal = accounts[acc_num].check_balance()
            print("Account balance is:", bal)
        else:
            print("Could not find account with number:", acc_num)

    elif choice == '5':
        # Exit the program
        print("Thanks for using our service!")
        break

    else:
        # Handle invalid menu options
        print("Invalid choice. Please try again.") 

