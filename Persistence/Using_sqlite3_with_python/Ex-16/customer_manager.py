import sqlite3

class CustomerManager:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the customers table if it does not exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        self.conn.commit()

    def insert_customers(self, customers_list):
        """Inserts multiple customers using a transaction"""
        try:
            self.conn.execute("BEGIN")  # Start transaction
            self.cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers_list)
            self.conn.commit()  # Commit transaction
            print("Transaction successful: All customers added.")
        except sqlite3.Error as e:
            self.conn.rollback()  # Rollback if error occurs
            print(f"Transaction failed! Rolled back. Error: {e}")

    def fetch_all_customers(self):
        """Fetches all customers"""
        self.cursor.execute("SELECT * FROM customers")
        data = self.cursor.fetchall()

        if not data:
            print("No customers found in the database.")
        else:
            for row in data:
                print(row)

    def close_connection(self):
        """Closes the database connection"""
        self.conn.close()
