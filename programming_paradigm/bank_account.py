# bank_account.py

class BankAccount:
    """A simple Bank Account class."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the given amount to the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account.
        Returns True if successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance (two decimal places)."""
        print(f"Current Balance: ${self.account_balance:.2f}")
