import sqlite3

def fetch_products():
    """Fetches and displays all products from the products table."""
    
    # Connect to the database
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Fetch all rows from the products table
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Display results
    if products:
        print("\n Products in the store:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: ₹{product[2]}")
    else:
        print(" No products found in the database.")

    
    conn.close()

# Run the function
if __name__ == "__main__":
    fetch_products()
