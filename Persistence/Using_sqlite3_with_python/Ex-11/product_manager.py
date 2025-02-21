import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price > 0)
            )
        """)
        self.conn.commit()

    def add_product(self, name, price):
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Product name must be a non-empty string.")
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Price must be a positive number.")

            self.conn.execute("BEGIN TRANSACTION;")  # Start transaction
            self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()  # Commit transaction
            print("Product added successfully.")

        except (sqlite3.Error, ValueError) as e:
            self.conn.rollback()  # Rollback transaction on error
            print(f"Error: {e}")

    def update_price(self, product_id, new_price):
        try:
            if not isinstance(new_price, (int, float)) or new_price <= 0:
                raise ValueError("Price must be a positive number.")

            self.conn.execute("BEGIN TRANSACTION;")
            self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
            self.conn.commit()
            print("Price updated successfully.")

        except (sqlite3.Error, ValueError) as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def delete_product(self, product_id):
        try:
            self.conn.execute("BEGIN TRANSACTION;")
            self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()
            print("Product deleted successfully.")

        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def search_product(self, name_fragment):
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
