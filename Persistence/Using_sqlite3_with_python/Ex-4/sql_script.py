import sqlite3

# Connect to SQLite database (creates 'store.db' if it doesn't exist)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Read the SQL script from file
with open("products_table.sql", "r") as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit and close
conn.commit()
conn.close()

print(" Table 'products' created successfully!")
