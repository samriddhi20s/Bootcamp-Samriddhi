import sqlite3

def insert_product(name, price):
    """Inserts a new product into the products table."""
    
    
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Insert data into the products table
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))

    
    conn.commit()
    conn.close()

    print(f"Product '{name}' added successfully!")

# Example usage (you can remove this and use it dynamically)
if __name__ == "__main__":
    insert_product("Laptop", 75000.00)
    insert_product("Mouse", 599.99)
