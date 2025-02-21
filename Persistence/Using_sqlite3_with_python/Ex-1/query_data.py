import sqlite3

# Connect to the database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Retrieve all data
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Display the data
print("Product List:")
print("ID | Name | Price | Quantity")
print("-" * 40)
for row in rows:
    print(row[0], "|", row[1], "|", row[2], "|", row[3])

# Close the connection
conn.close()
