class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True

        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True

        return False


# ######### Learning Signature #########
# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 3, 2026

# Program Description: This program creates an Account class that manages an account name and balance. It allows the user to check the balance, deposit money, and withdraw money while preventing invalid transactions.
# Reflection: I learned how to use classes and methods to manage an account balance. I also learned how to use conditions to make sure that deposits and withdrawals follow the given rules.

# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.