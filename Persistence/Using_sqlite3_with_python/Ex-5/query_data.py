import sqlite3

def fetch_products():
    """Fetches and displays all products from the products table."""
    
    # Connect to the database
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Fetch all records
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    
    if products:
        print("\n Products in the store:")
        print("-" * 40)
        print(f"{'ID':<5} {'Name':<20} {'Price':<10}")
        print("-" * 40)
        for product in products:
            print(f"{product[0]:<5} {product[1]:<20} ₹{product[2]:<10.2f}")
        print("-" * 40)
    else:
        print(" No products found in the database.")

    
    conn.close()


if __name__ == "__main__":
    fetch_products()
