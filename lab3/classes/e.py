class BankAccount:
    # Initialize account with owner and balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

    # Withdraw money, ensuring no overdraft
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"New balance: {self.balance}")

# Example usage:
account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail due to insufficient balance
