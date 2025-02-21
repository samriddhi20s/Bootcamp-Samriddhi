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

    def check_data_exists(self):
        self.cursor.execute("SELECT COUNT(*) FROM products")
        count = self.cursor.fetchone()[0]
        return count > 0

    def insert_sample_data(self):
        self.cursor.execute("INSERT INTO products (name, price) VALUES ('Smartphone', 45000.00)")
        self.cursor.execute("INSERT INTO products (name, price) VALUES ('Laptop', 75000.00)")
        self.conn.commit()

    def search_product(self, name_fragment):
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
