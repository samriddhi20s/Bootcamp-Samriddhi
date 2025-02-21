import sqlite3

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

    def add_category(self, name):
        try:
            self.conn.execute("BEGIN TRANSACTION;")
            self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            self.conn.commit()
            print(f"Category '{name}' added successfully.")
        except sqlite3.IntegrityError:
            self.conn.rollback()
            print(f"Category '{name}' already exists.")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def add_product(self, name, price, category_name):
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Product name must be a non-empty string.")
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Price must be a positive number.")

            self.conn.execute("BEGIN TRANSACTION;")
            self.cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
            category = self.cursor.fetchone()

            if category:
                category_id = category[0]
            else:
                self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
                category_id = self.cursor.lastrowid

            self.cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                                (name, price, category_id))
            self.conn.commit()
            print("Product added successfully.")

        except (sqlite3.Error, ValueError) as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def get_products_with_categories(self):
        self.cursor.execute("""
            SELECT p.id, p.name, p.price, c.name AS category 
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
        """)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
