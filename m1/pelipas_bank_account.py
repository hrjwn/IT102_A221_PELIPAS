from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        # Encapsulation
        self._pin = pin
        self._balance = max(0, starting_balance)

    # Encapsulation
    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        # Improvement: prevent invalid deposits
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):

        # Improvement: prevent invalid withdrawals
        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def verify_pin(self, pin):
        return self._pin == pin

    # Improvement: allow the account holder to change their PIN
    def change_pin(self, old_pin, new_pin):

        if self._pin != old_pin:
            return False

        if not new_pin.isdigit():
            return False

        if len(new_pin) != 4:
            return False

        self._pin = new_pin
        return True

    # Used by storage when the account
    # needs to be saved.
    def get_pin(self):
        return self._pin

    # Abstraction
    @abstractmethod
    def get_account_type(self):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):
        return "Savings Account"


# Inheritance
class StudentAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):
        return "Student Account"