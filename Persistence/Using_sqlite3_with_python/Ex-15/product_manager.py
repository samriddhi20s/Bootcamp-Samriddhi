import sqlite3
import csv

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price > 0),
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
            )
        """)
        self.conn.commit()

    def add_products_batch(self, products_list):
        """Inserts multiple products in one transaction"""
        try:
            self.conn.execute("BEGIN")  # Start transaction
            for name, price, category_name in products_list:
                # Insert category if not exists
                self.cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category_name,))
                self.cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
                category_id = self.cursor.fetchone()[0]

                # Insert product
                self.cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", 
                                    (name, price, category_id))
            self.conn.commit()  # Commit transaction
            print("Batch insertion successful.")
        except sqlite3.Error as e:
            self.conn.rollback()  # Rollback if error occurs
            print(f"Database error: {e}")

    def fetch_all_products(self):
        """Fetches all products and prints them"""
        self.cursor.execute("""
            SELECT products.id, products.name, products.price, categories.name 
            FROM products 
            LEFT JOIN categories ON products.category_id = categories.id
        """)
        data = self.cursor.fetchall()

        if not data:
            print("No products found in the database.")
        else:
            for row in data:
                print(row)

    def close_connection(self):
        """Closes the database connection"""
        self.conn.close()
