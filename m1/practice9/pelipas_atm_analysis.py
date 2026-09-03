def analyze_transactions():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        return {
            "Total Transactions": 0,
            "Deposits": 0,
            "Withdrawals": 0,
            "Total Deposited": 0,
            "Total Withdrawn": 0,
            "Average Transaction": 0,
            "Latest Transaction": None,
            "Latest Timestamp": None,
            "Largest Transaction": 0
        }

    transactions = []
    current = {}

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("Timestamp:"):
            current["timestamp"] = line.replace("Timestamp:", "").strip()

        elif line.startswith("Account:"):
            current["account"] = line.replace("Account:", "").strip()

        elif line.startswith("Transaction:"):
            current["transaction"] = line.replace("Transaction:", "").strip()

        elif line.startswith("Amount:"):
            amount = line.replace("Amount:", "").strip()
            amount = amount.replace("₱", "").replace(",", "")
            current["amount"] = float(amount)

            if "timestamp" in current and "account" in current and "transaction" in current:
                transactions.append(current)
                current = {}

    total_transactions = len(transactions)

    deposits = 0
    withdrawals = 0
    total_deposited = 0
    total_withdrawn = 0
    largest_transaction = 0

    for transaction in transactions:
        amount = transaction["amount"]

        if transaction["transaction"] == "Deposit":
            deposits += 1
            total_deposited += amount

        elif transaction["transaction"] == "Withdraw":
            withdrawals += 1
            total_withdrawn += amount

        if amount > largest_transaction:
            largest_transaction = amount

    if total_transactions > 0:
        average_transaction = (
            total_deposited + total_withdrawn
        ) / total_transactions

        latest_transaction = transactions[-1]["transaction"]
        latest_timestamp = transactions[-1]["timestamp"]

    else:
        average_transaction = 0
        latest_transaction = None
        latest_timestamp = None

    return {
        "Total Transactions": total_transactions,
        "Deposits": deposits,
        "Withdrawals": withdrawals,
        "Total Deposited": total_deposited,
        "Total Withdrawn": total_withdrawn,
        "Average Transaction": average_transaction,
        "Latest Transaction": latest_transaction,
        "Latest Timestamp": latest_timestamp,
        "Largest Transaction": largest_transaction
    }


######### Learning Signature #########
# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 3, 2026
#
# Program Description: This program analyzes ATM transaction records and calculates the total transactions, deposits, withdrawals, transaction amounts, latest transaction, and largest transaction.
# Reflection: I learned how to read and process transaction records from a text file. I also learned how to use lists, dictionaries, loops, and conditions to calculate different transaction statistics.
#
# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.