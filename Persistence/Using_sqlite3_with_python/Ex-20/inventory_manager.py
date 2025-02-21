import sqlite3
from datetime import datetime

class InventoryManager:
    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates products and inventory_log tables"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                stock INTEGER NOT NULL CHECK (stock >= 0)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory_log (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                change INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)
        self.conn.commit()

    def add_product(self, name, stock):
        """Adds a new product"""
        try:
            self.cursor.execute("INSERT INTO products (name, stock) VALUES (?, ?)", (name, stock))
            self.conn.commit()
            print(f"Product '{name}' added with stock {stock}.")
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def update_stock(self, product_id, change):
        """Updates stock and logs the change in a transaction"""
        try:
            self.conn.execute("BEGIN")

            # Fetch current stock
            self.cursor.execute("SELECT stock FROM products WHERE product_id = ?", (product_id,))
            result = self.cursor.fetchone()

            if result is None:
                raise ValueError("Product not found.")
            
            new_stock = result[0] + change
            if new_stock < 0:
                raise ValueError("Insufficient stock!")

            # Update stock
            self.cursor.execute("UPDATE products SET stock = ? WHERE product_id = ?", (new_stock, product_id))

            # Log the change
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("INSERT INTO inventory_log (product_id, change, timestamp) VALUES (?, ?, ?)",
                                (product_id, change, timestamp))

            self.conn.commit()
            print(f"Stock updated successfully. New stock: {new_stock}")

        except (sqlite3.Error, ValueError) as e:
            self.conn.rollback()
            print(f"Transaction failed! Rolled back. Error: {e}")

    def fetch_inventory(self):
        """Fetches and displays product inventory"""
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        if not products:
            print("No products available.")
        else:
            for product in products:
                print(product)

    def fetch_logs(self):
        self.cursor.execute("SELECT * FROM inventory_log")
        logs = self.cursor.fetchall()

        if not logs:
            print("No inventory logs found.")
        else:
            for log in logs:
                print(log)

    def close_connection(self):
        self.conn.close()
