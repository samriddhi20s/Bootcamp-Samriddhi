import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()


cursor.execute()

# Insert 500 records
for i in range(1, 501):
    company_name = f"Company_{i}"
    cursor.execute("INSERT INTO COMPANIES (company_name, id) VALUES (?, ?)", (company_name, i))

conn.commit()
conn.close()

print("500 records inserted successfully into COMPANIES table.")
