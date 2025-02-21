import sqlite3

class BankingManager:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_accounts_table()

    def create_accounts_table(self):
        """Creates the accounts table if it does not exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL CHECK (balance >= 0)
            )
        """)
        self.conn.commit()

    def create_accounts(self):
        """Insert initial accounts (for testing)"""
        try:
            self.cursor.executemany("INSERT INTO accounts (name, balance) VALUES (?, ?)", [
                ("Alice", 5000.00),
                ("Bob", 3000.00)
            ])
            self.conn.commit()
            print("Initial accounts created.")
        except sqlite3.Error as e:
            print(f"Error inserting accounts: {e}")

    def transfer_funds(self, from_acc, to_acc, amount):
        """Transfers money between two accounts within a transaction"""
        try:
            self.conn.execute("BEGIN")  # Start transaction

            # Check sender's balance
            self.cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_acc,))
            sender_balance = self.cursor.fetchone()
            if sender_balance is None:
                raise ValueError("Sender account does not exist.")
            if sender_balance[0] < amount:
                raise ValueError("Insufficient balance.")

            # Deduct from sender
            self.cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_acc))

            # Add to receiver
            self.cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_acc))

            self.conn.commit()  # Commit transaction if both operations succeed
            print(f"Transfer of ₹{amount} from Account {from_acc} to Account {to_acc} successful.")

        except (sqlite3.Error, ValueError) as e:
            self.conn.rollback()  # Rollback if any error occurs
            print(f"Transaction failed! Rolled back. Error: {e}")

    def fetch_accounts(self):
        self.cursor.execute("SELECT * FROM accounts")
        data = self.cursor.fetchall()

        if not data:
            print("No accounts found.")
        else:
            for row in data:
                print(row)

    def close_connection(self):
        self.conn.close()
