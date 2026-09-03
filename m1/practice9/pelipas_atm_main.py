import streamlit as st

from pelipas_atm_account import Account
import pelipas_atm_balance as balance
import pelipas_atm_deposit as deposit
import pelipas_atm_withdraw as withdraw
import pelipas_atm_history as history
import pelipas_atm_analysis as analysis


account = Account("Juan Dela Cruz", 10000)


st.set_page_config(
    page_title="ATM System",
    page_icon="🏦",
    layout="wide"
)


st.title("🏧 ATM System")
st.write(f"Welcome, {account.account_name}!")

st.divider()


st.sidebar.title("ATM Menu")

choice = st.sidebar.radio(
    "Select an operation:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)


if choice == "Check Balance":

    st.header("Check Balance")

    current_balance = balance.check_balance(account)

    st.metric(
        "Current Balance",
        f"₱{current_balance:,.2f}"
    )


elif choice == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount:",
        min_value=0.0,
        step=100.0
    )

    if st.button("Deposit"):
        if amount <= 0:
            st.error("Invalid deposit amount.")
        else:
            result = deposit.deposit_money(account, amount)

            if result:
                st.success(
                    f"Deposit successful! New Balance: ₱{account.check_balance():,.2f}"
                )
            else:
                st.error("Deposit failed.")


elif choice == "Withdraw":

    st.header("Withdraw Money")

    amount = st.number_input(
        "Enter withdrawal amount:",
        min_value=0.0,
        step=100.0
    )

    if st.button("Withdraw"):
        if amount <= 0:
            st.error("Invalid withdrawal amount.")
        elif amount > account.check_balance():
            st.error("Insufficient balance.")
        else:
            result = withdraw.withdraw_money(account, amount)

            if result:
                st.success(
                    f"Withdrawal successful! New Balance: ₱{account.check_balance():,.2f}"
                )
            else:
                st.error("Withdrawal failed.")


elif choice == "View History":

    st.header("Transaction History")

    transactions = history.view_history()

    if transactions:
        st.text("".join(transactions))
    else:
        st.info("No transactions found.")


elif choice == "Analyze Transactions":

    st.header("📊 Transaction Analysis")

    results = analysis.analyze_transactions()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Transactions",
            results["Total Transactions"]
        )

        st.metric(
            "Deposits",
            results["Deposits"]
        )

        st.metric(
            "Withdrawals",
            results["Withdrawals"]
        )

    with col2:
        st.metric(
            "Total Deposited",
            f"₱{results['Total Deposited']:,.2f}"
        )

        st.metric(
            "Total Withdrawn",
            f"₱{results['Total Withdrawn']:,.2f}"
        )

        st.metric(
            "Average Transaction",
            f"₱{results['Average Transaction']:,.2f}"
        )

    with col3:
        st.metric(
            "Largest Transaction",
            f"₱{results['Largest Transaction']:,.2f}"
        )

        st.write("**Latest Transaction:**")
        st.write(results["Latest Transaction"])

        st.write("**Latest Timestamp:**")
        st.write(results["Latest Timestamp"])


######### Learning Signature #########
# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 3, 2026
#
# Program Description: This program creates a Streamlit-based ATM application that allows users to check their balance, deposit money, withdraw money, view transaction history, and analyze transactions.
#
# Reflection: I learned how to connect different Python modules and use Streamlit to create an interactive ATM application. I also learned how an Account object can be shared between modules to perform different ATM operations.
#
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.