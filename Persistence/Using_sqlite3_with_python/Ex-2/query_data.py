import sqlite3

# Connect to the database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Check if 'products' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
table_exists = cursor.fetchone()

if table_exists:
    print(" The 'products' table exists in the database.")
else:
    print(" The 'products' table was not created!")

# Close the connection
conn.close()
