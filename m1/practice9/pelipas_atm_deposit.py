from datetime import datetime


def deposit_money(account, amount):
    if amount <= 0:
        return False

    result = account.deposit(amount)

    if result:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.txt", "a") as file:
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Account: {account.account_name}\n")
            file.write("Transaction: Deposit\n")
            file.write(f"Amount: ₱{amount:.2f}\n")
            file.write("\n")

        return True

    return False


######### Learning Signature #########
# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 3, 2026
#
# Program Description: This program handles account deposits by validating the amount, updating the account balance, recording the transaction with a timestamp, and saving it to a text file.
#
# Reflection: I learned how to use datetime to create timestamps and how to write deposit transactions to a text file. I also learned how to pass an Account object and amount to a function.
#
# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.