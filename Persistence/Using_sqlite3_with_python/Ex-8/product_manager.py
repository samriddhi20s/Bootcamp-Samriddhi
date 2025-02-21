import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f" Database connection error: {e}")

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f" Table creation error: {e}")

    def add_product(self, name, price):
        try:
            self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
            print(f" Product '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f" Error adding product: {e}")

    def update_product(self, product_id, new_price):
        try:
            self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f" Updated product ID {product_id} to price {new_price}.")
            else:
                print(f" Product ID {product_id} not found.")
        except sqlite3.Error as e:
            print(f" Error updating product: {e}")

    def delete_product(self, product_id):
        try:
            self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f" Deleted product ID {product_id}.")
            else:
                print(f" Product ID {product_id} not found.")
        except sqlite3.Error as e:
            print(f" Error deleting product: {e}")

    def list_products(self):
        try:
            self.cursor.execute("SELECT * FROM products")
            products = self.cursor.fetchall()
            if products:
                for p in products:
                    print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]}")
            else:
                print(" No products found.")
        except sqlite3.Error as e:
            print(f" Error fetching products: {e}")

    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f" Error closing connection: {e}")
