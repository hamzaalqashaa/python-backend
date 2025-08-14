# ---------------------------
# Base Class: Account
# ---------------------------
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method (default behavior)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds or invalid amount.")

    # Display balance
    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.__balance:.2f}")

    # Getter for private balance
    def _get_balance(self):
        return self.__balance

    # Setter for private balance
    def _set_balance(self, amount):
        self.__balance = amount

    # Magic method for readable print
    def __str__(self):
        return f"Account({self.account_number}, Holder: {self.account_holder}, Balance: ${self.__balance:.2f})"

    # Magic method for equality comparison
    def __eq__(self, other):
        if isinstance(other, Account):
            return self.account_number == other.account_number
        return False


# ---------------------------
# Subclass: SavingsAccount
# ---------------------------
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # Override withdraw: must maintain at least $100
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self._get_balance() - amount < 100:
            print("Cannot withdraw: Minimum balance of $100 must be maintained.")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"Withdrew ${amount:.2f} from savings account.")


# ---------------------------
# Subclass: CheckingAccount
# ---------------------------
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Override withdraw: allow negative balance within overdraft limit
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self._get_balance() - amount < -self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"Withdrew ${amount:.2f} from checking account.")


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    # Create accounts
    savings = SavingsAccount("SA001", "Alice", 500, interest_rate=0.03)
    checking = CheckingAccount("CA001", "Bob", 200, overdraft_limit=300)

    # Test deposits and withdrawals
    savings.deposit(100)
    savings.withdraw(450)  # Should fail (balance < 100)
    savings.withdraw(200)  # Should pass

    checking.deposit(50)
    checking.withdraw(600)  # Should fail (overdraft exceeded)
    checking.withdraw(400)  # Should pass

    # Display balances
    savings.display_balance()
    checking.display_balance()

    # Magic methods
    print(savings)
    print(checking)
    print("Accounts equal?", savings == checking)
    print("Accounts equal?", savings == SavingsAccount("SA001", "Alice", 300))
