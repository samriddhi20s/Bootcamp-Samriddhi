import sqlite3

class ProductManager:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the products table if it does not exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK (price > 0)
            )
        """)
        self.conn.commit()

    def batch_insert_products(self, products):
        """Inserts multiple products in a single transaction"""
        try:
            self.conn.execute("BEGIN")  # Start transaction
            
            self.cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
            
            self.conn.commit()  # Commit if all insertions are successful
            print("Batch insert successful!")

        except sqlite3.Error as e:
            self.conn.rollback()  # Rollback if any error occurs
            print(f"Transaction failed! Rolled back. Error: {e}")

    def fetch_products(self):
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()

        if not data:
            print("No products found in the database.")
        else:
            for row in data:
                print(row)

    def close_connection(self):
        self.conn.close()
