import sqlite3

def check_table():
    """Checks if the 'products' table exists in the database."""
    

    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
    table_exists = cursor.fetchone()

    if table_exists:
        print("The 'products' table exists.")
    else:
        print("The 'products' table does NOT exist. Run sql_script.py first.")

    
    conn.close()


if __name__ == "__main__":
    check_table()
