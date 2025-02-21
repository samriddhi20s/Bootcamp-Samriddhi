import sqlite3

def delete_product(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"✅ Deleted product with ID {product_id}")
    else:
        print(f"⚠️ No product found with ID {product_id}")

    conn.close()

if __name__ == "__main__":
    product_id = int(input("Enter Product ID to delete: "))
    delete_product(product_id)
