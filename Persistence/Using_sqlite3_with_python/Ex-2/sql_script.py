import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Read the SQL script
with open('create_products_table.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

print("Table 'products' created successfully!")

# Commit changes and close the connection
conn.commit()
conn.close()
