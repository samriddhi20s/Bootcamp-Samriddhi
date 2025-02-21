import sqlite3

class OrderManager:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the orders and order_details tables if they do not exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_details (
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    def insert_sample_data(self):
        """Insert sample data into orders and order_details"""
        self.cursor.execute("INSERT INTO orders (customer_name, status) VALUES ('John Doe', 'Pending')")
        order_id = self.cursor.lastrowid  # Get the last inserted order ID

        order_details = [
            (order_id, "Laptop", 1, 75000.00),
            (order_id, "Mouse", 2, 1500.00)
        ]
        self.cursor.executemany("INSERT INTO order_details (order_id, product_name, quantity, price) VALUES (?, ?, ?, ?)", order_details)

        self.conn.commit()
        print("Sample data inserted.")

    def update_order_transaction(self, order_id, new_status, product_name, new_quantity, new_price):
        """Updates order status and order details within a transaction"""
        try:
            self.conn.execute("BEGIN")  # Start transaction
            
            # Update order status
            self.cursor.execute("UPDATE orders SET status = ? WHERE order_id = ?", (new_status, order_id))
            
            # Update order details (quantity and price)
            self.cursor.execute("UPDATE order_details SET quantity = ?, price = ? WHERE order_id = ? AND product_name = ?", 
                                (new_quantity, new_price, order_id, product_name))

            self.conn.commit()  # Commit transaction
            print("Transaction successful: Orders and order details updated.")

        except sqlite3.Error as e:
            self.conn.rollback()  # Rollback if error occurs
            print(f"Transaction failed! Rolled back. Error: {e}")

    def fetch_orders(self):
        """Fetches and displays orders with their details"""
        self.cursor.execute("""
            SELECT o.order_id, o.customer_name, o.status, d.product_name, d.quantity, d.price 
            FROM orders o
            JOIN order_details d ON o.order_id = d.order_id
        """)
        data = self.cursor.fetchall()

        if not data:
            print("No orders found in the database.")
        else:
            for row in data:
                print(row)

    def close_connection(self):
        """Closes the database connection"""
        self.conn.close()
