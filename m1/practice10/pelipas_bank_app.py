import streamlit as st

import pelipas_bank_auth
import pelipas_bank_storage
import pelipas_bank_transactions
import pelipas_bank_analysis
import pelipas_bank_utils


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Pelipas Bank",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# CUSTOM GUI DESIGN
# ==========================================

st.markdown("""
<style>

/* ==============================
   GENERAL THEME
   ============================== */

.stApp {
    background-color: var(--background-color);
    color: var(--text-color);
}

/* Main headings - ALWAYS BLUE */
h1, h2, h3 {
    color: #0b5ed7;
    font-weight: 800;
}

/* Normal text follows theme */
p, label, span {
    color: var(--text-color);
}

/* Captions */
div[data-testid="stCaptionContainer"] {
    color: var(--text-color);
    opacity: 0.75;
}


/* ==============================
   BLUE BUTTONS
   ============================== */

/* Login, Register, Deposit, Withdraw buttons */
.stButton > button {
    background-color: #0b5ed7;
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    transition: 0.2s;
}

/* Button hover */
.stButton > button:hover {
    background-color: #084298;
    color: white !important;
    border: none;
}


/* ==============================
   SIDEBAR
   ============================== */

[data-testid="stSidebar"] {
    background-color: var(--secondary-background-color);
}

/* Sidebar text follows theme */
[data-testid="stSidebar"] * {
    color: var(--text-color);
}

/* Sidebar title stays BLUE */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #0b5ed7;
}


/* ==============================
   INPUT BOXES
   ============================== */

.stTextInput input,
.stNumberInput input {
    border-radius: 8px;
}


/* ==============================
   METRIC CARDS
   ============================== */

[data-testid="stMetric"] {
    background-color: var(--secondary-background-color);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(128, 128, 128, 0.25);
}

/* Metric values stay BLUE */
[data-testid="stMetricValue"] {
    color: #0b5ed7;
}


/* ==============================
   CUSTOM BANK CARDS
   ============================== */

.bank-card {
    background-color: var(--secondary-background-color);
    color: var(--text-color);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    margin-bottom: 20px;
}

.bank-card-title {
    color: #0b5ed7;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.bank-card-text {
    color: var(--text-color);
    opacity: 0.75;
    font-size: 14px;
}


/* ==============================
   BLUE ICONS / ACCENTS
   ============================== */

.blue-icon {
    color: #0b5ed7;
    font-size: 28px;
    font-weight: bold;
}


/* ==============================
   SUCCESS / INFO BOXES
   ============================== */

[data-testid="stAlert"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)




# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if "account" not in st.session_state:
    st.session_state.account = None


# ==========================================
# BANK HEADER
# ==========================================

st.title("🏦 PELIPAS BANK")
st.caption("💙 Secure • Simple • Smart Digital Banking")
st.divider()


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        [
            "🔐 Login",
            "📝 Register"
        ]
    )


    # ======================================
    # LOGIN
    # ======================================

    with login_tab:

        st.subheader("🔐 Welcome Back!")

        st.write(
            "Access your account securely using "
            "your account number and PIN."
        )

        account_number = st.text_input(
            "Account Number",
            key="login_account",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="login_pin",
            placeholder="Enter your 4-digit PIN"
        )

        if st.button(
            "🔓 Login",
            use_container_width=True
        ):

            account, message = (
                pelipas_bank_auth
                .login_account(
                    account_number,
                    pin
                )
            )

            if account is not None:

                st.session_state.logged_in = True

                st.session_state.account = (
                    account
                )

                st.success(message)

                st.rerun()

            else:

                st.error(message)


    # ======================================
    # REGISTRATION
    # ======================================

    with register_tab:

        st.subheader(
            "📝 Create Your Bank Account"
        )

        st.write(
            "Fill in the information below to "
            "create your digital bank account."
        )

        name = st.text_input(
            "Full Name",
            key="register_name",
            placeholder="Enter your full name"
        )

        account_number = st.text_input(
            "Account Number",
            key="register_account",
            placeholder="Create an account number"
        )

        pin = st.text_input(
            "Create 4-Digit PIN",
            type="password",
            key="register_pin",
            placeholder="Enter a 4-digit PIN"
        )

        confirm_pin = st.text_input(
            "Confirm PIN",
            type="password",
            key="register_confirm_pin",
            placeholder="Re-enter your PIN"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Savings Account",
                "Student Account"
            ]
        )

        starting_balance = st.number_input(
            "Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button(
            "✨ Create Account",
            use_container_width=True
        ):

            account, message = (
                pelipas_bank_auth
                .register_account(
                    name,
                    account_number,
                    pin,
                    confirm_pin,
                    account_type,
                    starting_balance
                )
            )

            if account is not None:

                st.success(message)

                st.info(
                    "Your account has been created. "
                    "Please use the Login tab to access "
                    "your account."
                )

            else:

                st.error(message)


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )


    # ======================================
    # SIDEBAR
    # ======================================

    st.sidebar.title(
        "🏦 PELIPAS BANK"
    )

    st.sidebar.caption(
        "Your Digital Banking Hub"
    )

    st.sidebar.divider()

    st.sidebar.write(
        f"👤 **{account.account_name}**"
    )

    st.sidebar.caption(
        account.get_account_type()
    )

    st.sidebar.write(
        f"💳 Account: "
        f"{account.account_number}"
    )

    st.sidebar.divider()


    menu = st.sidebar.radio(
        "BANKING MENU",
        [
            "🏠 Dashboard",
            "💰 Deposit",
            "💸 Withdraw",
            "📜 Transaction History",
            "📊 Transaction Analysis"
        ]
    )


    st.sidebar.divider()


    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.rerun()


    # ======================================
    # DASHBOARD
    # ======================================

    if menu == "🏠 Dashboard":

        st.header(
            f"👋 Welcome, {account.account_name}!"
        )

        st.write(
            "Here is an overview of your "
            "Pelipas Bank account."
        )

        st.divider()

        st.subheader(
            "💳 Account Overview"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "💰 Current Balance",
            pelipas_bank_utils
            .format_currency(
                account.check_balance()
            )
        )


        col2.metric(
            "🏦 Account Type",
            account.get_account_type()
        )


        col3.metric(
            "💳 Account Number",
            account.account_number
        )


        st.divider()


        st.markdown(
            """
            <div class="bank-card">

            <div class="bank-card-title">
            🏦 Welcome to Pelipas Bank
            </div>

            <div class="bank-card-text">
            Manage your money easily and securely.
            Use the banking menu on the left to
            deposit money, withdraw money, view your
            transaction history, or analyze your
            account activity.
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.info(
            "💡 Select a banking service from "
            "the menu on the left."
        )


    # ======================================
    # DEPOSIT
    # ======================================

    elif menu == "💰 Deposit":

        st.header(
            "💰 Deposit Money"
        )

        st.write(
            "Add money to your bank account."
        )

        st.divider()


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Current Balance",
                pelipas_bank_utils
                .format_currency(
                    account.check_balance()
                )
            )


        with col2:

            st.info(
                "Enter the amount you want "
                "to deposit below."
            )


        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "💰 Confirm Deposit",
            use_container_width=True
        ):

            if not pelipas_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "❌ Invalid deposit amount."
                )

            else:

                success = account.deposit(
                    amount
                )


                if success:

                    pelipas_bank_storage.update_account(
                        account
                    )


                    pelipas_bank_transactions.record_transaction(
                        account,
                        "Deposit",
                        amount
                    )


                    st.success(
                        "✅ Deposit successful!"
                    )


                    st.metric(
                        "💵 New Balance",
                        pelipas_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # WITHDRAW
    # ======================================

    elif menu == "💸 Withdraw":

        st.header(
            "💸 Withdraw Money"
        )

        st.write(
            "Withdraw money from your bank account."
        )

        st.divider()


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Available Balance",
                pelipas_bank_utils
                .format_currency(
                    account.check_balance()
                )
            )


        with col2:

            st.info(
                "Make sure you have enough "
                "balance before withdrawing."
            )


        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "💸 Confirm Withdrawal",
            use_container_width=True
        ):

            if not pelipas_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "❌ Invalid withdrawal amount."
                )

            elif amount > account.check_balance():

                st.error(
                    "⚠️ Insufficient balance."
                )

            else:

                success = account.withdraw(
                    amount
                )


                if success:

                    pelipas_bank_storage.update_account(
                        account
                    )


                    pelipas_bank_transactions.record_transaction(
                        account,
                        "Withdraw",
                        amount
                    )


                    st.success(
                        "✅ Withdrawal successful!"
                    )


                    st.metric(
                        "💵 New Balance",
                        pelipas_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # TRANSACTION HISTORY
    # ======================================

    elif menu == "📜 Transaction History":

        st.header(
            "📜 Transaction History"
        )

        st.write(
            "Review your previous deposits "
            "and withdrawals."
        )

        st.divider()


        transactions = (
            pelipas_bank_transactions
            .get_transactions()
        )


        # Show only transactions
        # belonging to the logged-in user.

        transactions = [
            transaction
            for transaction in transactions
            if transaction.get(
                "account_number"
            ) == account.account_number
        ]


        if transactions:

            display_data = []


            for transaction in transactions:

                display_data.append({

                    "Timestamp":
                        transaction.get(
                            "timestamp",
                            "N/A"
                        ),

                    "Transaction":
                        transaction.get(
                            "transaction",
                            "N/A"
                        ),

                    "Amount":
                        pelipas_bank_utils
                        .format_currency(
                            transaction.get(
                                "amount",
                                0
                            )
                        ),

                    "Balance After":
                        pelipas_bank_utils
                        .format_currency(
                            transaction.get(
                                "balance_after",
                                0
                            )
                        )
                })


            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True
            )


        else:

            st.info(
                "📭 No transaction history available."
            )


    # ======================================
    # TRANSACTION ANALYSIS
    # ======================================

    elif menu == "📊 Transaction Analysis":

        st.header(
            "📊 Transaction Analysis"
        )

        st.write(
            "View a summary of your banking activity "
            "and money flow."
        )

        st.divider()


        result = (
            pelipas_bank_analysis
            .analyze_transactions(
                account.account_number
            )
        )


        # ==================================
        # ANALYSIS 1
        # TRANSACTION SUMMARY
        # ==================================

        st.subheader(
            "1️⃣ Transaction Summary"
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "📋 Total Transactions",
            result[
                "total_transactions"
            ]
        )


        col2.metric(
            "💰 Deposits",
            result[
                "deposits"
            ]
        )


        col3.metric(
            "💸 Withdrawals",
            result[
                "withdrawals"
            ]
        )


        st.divider()


        # ==================================
        # ANALYSIS 2
        # MONEY FLOW
        # ==================================

        st.subheader(
            "2️⃣ Money Flow Analysis"
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "💰 Total Deposited",
            pelipas_bank_utils
            .format_currency(
                result[
                    "total_deposited"
                ]
            )
        )


        col2.metric(
            "💸 Total Withdrawn",
            pelipas_bank_utils
            .format_currency(
                result[
                    "total_withdrawn"
                ]
            )
        )


        col3.metric(
            "📈 Net Cash Flow",
            pelipas_bank_utils
            .format_currency(
                result[
                    "net_cash_flow"
                ]
            )
        )


        st.divider()


        # ==================================
        # ANALYSIS 3
        # ACCOUNT ACTIVITY
        # ==================================

        st.subheader(
            "3️⃣ Account Activity Analysis"
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "🔝 Largest Transaction",
            pelipas_bank_utils
            .format_currency(
                result[
                    "largest_transaction"
                ]
            )
        )


        col2.metric(
            "📊 Average Transaction",
            pelipas_bank_utils
            .format_currency(
                result[
                    "average_transaction"
                ]
            )
        )


        col3.metric(
            "📝 Latest Transaction",
            result[
                "latest_transaction"
            ]
        )


        st.divider()


        st.info(
            f"🕒 Latest Activity: "
            f"{result['latest_timestamp']}"
        )

# ######### Learning Signature #########

# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 4, 2026

# Program Description:
# This program is a graphical banking application
# that allows users to register, log in, check their
# balance, deposit money, withdraw money, view
# transaction history and analyze transactions.

# Reflection:
# I learned how Streamlit can be used to create a
# simple and user-friendly banking interface while
# keeping the existing OOP structure of the program.

# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.