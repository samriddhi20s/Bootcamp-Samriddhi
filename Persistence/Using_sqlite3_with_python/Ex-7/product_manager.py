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
                price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()
        print(f"Product '{name}' added successfully.")

    def update_product(self, product_id, new_price):
        self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f" Updated product ID {product_id} to price {new_price}.")
        else:
            print(f" Product ID {product_id} not found.")

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f" Deleted product ID {product_id}.")
        else:
            print(f" Product ID {product_id} not found.")

    def list_products(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        if products:
            for p in products:
                print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]}")
        else:
            print(" No products found.")

    def close_connection(self):
        self.conn.close()
