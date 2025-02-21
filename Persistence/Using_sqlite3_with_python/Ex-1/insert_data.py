import sqlite3

# Connect to the database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Insert sample data
products = [
    ("Laptop", 75000, 10),
    ("Mouse", 500, 50),
    ("Keyboard", 1500, 30),
    ("Monitor", 12000, 20)
]

cursor.executemany('''
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
''', products)

print("Data inserted successfully!")

# Commit and close
conn.commit()
conn.close()
