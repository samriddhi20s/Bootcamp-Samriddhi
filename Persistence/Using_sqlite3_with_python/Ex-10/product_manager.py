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

    def validate_product(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        return True

    def add_product(self, name, price):
        try:
            self.validate_product(name, price)
            self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
            print("Product added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def update_price(self, product_id, new_price):
        try:
            if not isinstance(new_price, (int, float)) or new_price <= 0:
                raise ValueError("Price must be a positive number.")
            
            self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
            self.conn.commit()
            print("Price updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def search_product(self, name_fragment):
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
