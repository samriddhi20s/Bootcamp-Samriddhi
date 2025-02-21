import sqlite3

def update_product_price(product_id, new_price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Updated product ID {product_id} to new price ₹{new_price:.2f}")
    else:
        print(f"No product found with ID {product_id}")

    conn.close()

if __name__ == "__main__":
    product_id = int(input("Enter Product ID to update: "))
    new_price = float(input("Enter New Price: "))
    update_product_price(product_id, new_price)
