import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Create a table for products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

print("Table 'products' created successfully!")

# Commit changes and close the connection
conn.commit()
conn.close()
