import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "transactions.json")

# ----------------- Helper Functions -----------------
def load_data():
    """Load transactions from file if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Error reading data file. Starting fresh.")
    return []


def save_data(transactions):
    """Save transactions to file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(transactions, file, indent=4)
    except IOError:
        print("⚠️ Error saving data.")


def add_transaction(transactions):
    """Add a new income or expense transaction."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Salary, Groceries, Rent): ").strip()
        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()

        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")

        transaction = {
            "amount": amount,
            "category": category,
            "date": date_str
        }

        transactions.append(transaction)
        save_data(transactions)
        print("✅ Transaction added successfully!")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.")


def view_transactions(transactions):
    """Display all recorded transactions."""
    if not transactions:
        print("📭 No transactions found.")
        return

    print("\n--- Transaction List ---")
    for idx, txn in enumerate(transactions, start=1):
        t_type = "Income" if txn["amount"] > 0 else "Expense"
        print(f"{idx}. {txn['date']} | {txn['category']} | {t_type} | ${txn['amount']:.2f}")
    print("-------------------------\n")


def financial_summary(transactions):
    """Calculate and display summary of income, expenses, and net balance."""
    total_income = sum(txn["amount"] for txn in transactions if txn["amount"] > 0)
    total_expenses = sum(txn["amount"] for txn in transactions if txn["amount"] < 0)
    net_balance = total_income + total_expenses

    print("\n--- Financial Summary ---")
    print(f"Total Income : ${total_income:.2f}")
    print(f"Total Expenses: ${abs(total_expenses):.2f}")
    print(f"Net Balance  : ${net_balance:.2f}")
    print("-------------------------\n")


# ----------------- Main CLI Loop -----------------
def main():
    transactions = load_data()

    while True:
        print("📊 Personal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Financial Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            financial_summary(transactions)
        elif choice == "4":
            print("💾 Exiting... Your data has been saved.")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()
