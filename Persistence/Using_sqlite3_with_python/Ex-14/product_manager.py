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

    def add_product(self, name, price, category_name):
        """Inserts a product with a category into the database"""
        try:
            # Insert category if not exists
            self.cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category_name,))
            self.cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
            category_id = self.cursor.fetchone()[0]

            # Insert product
            self.cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", 
                                (name, price, category_id))
            self.conn.commit()
            print(f"Product '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def export_to_csv(self, filename="products_export.csv"):
        """Exports product data to a CSV file"""
        try:
            self.cursor.execute("""
                SELECT products.id, products.name, products.price, categories.name 
                FROM products 
                LEFT JOIN categories ON products.category_id = categories.id
            """)
            data = self.cursor.fetchall()

            if not data:
                print("No data found in the products table.")
                return

            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Product Name", "Price", "Category"])
                writer.writerows(data)

            print(f"Data successfully exported to {filename}")

        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def close_connection(self):
        """Closes the database connection"""
        self.conn.close()
