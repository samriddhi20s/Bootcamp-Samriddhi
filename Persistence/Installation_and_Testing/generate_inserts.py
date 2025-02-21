import random

with open("insert_statements.sql", "w") as f:
    for i in range(1, 501):  # Generating 500 entries
        company_name = f"Company_{i}"
        sql = f'INSERT INTO COMPANIES (company_name, id) VALUES ("{company_name}", {i});\n'
        f.write(sql)

print("SQL insert statements file created: insert_statements.sql")
