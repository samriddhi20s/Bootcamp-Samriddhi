# Persistence Notes

## Concepts to Learn
- Understanding SQLite and its integration with Python.
- Performing CRUD operations using sqlite3.
- Advanced SQLite features for optimized performance.

## Tasks & Approaches

### SQLite
Exploring SQLite as a lightweight database solution.

### Preparation of the System
Ensuring necessary dependencies and environment setup for SQLite usage.

### Installation and Testing
Installing SQLite and verifying proper functionality.

### Using sqlite3 with Python
Connecting to SQLite databases, performing queries, and handling transactions.

### Advanced Python Usage
Leveraging Python for optimized database management and advanced querying techniques.

## Errors Faced & Solutions

### Error 1: No module named 'sqlite3'
**Solution:** Ensure that SQLite is installed and Python is compiled with SQLite support. Run:
```sh
pip install pysqlite3
```
if needed.

### Error 2: sqlite3.OperationalError: unable to open database file
**Solution:** Verify the database path, check permissions, and ensure the directory exists.

### Error 3: sqlite3.IntegrityError: UNIQUE constraint failed
**Solution:** Ensure unique constraints are properly handled using:
```sql
INSERT OR IGNORE
```
or
```sql
UPSERT
```
strategies.

## What I Learned
- How to set up and use SQLite databases efficiently.
- Best practices for database transactions and error handling.
- Advanced SQLite querying techniques and optimizations.

## ChatGPT Assistance
ChatGPT helped debug errors, optimize queries, and suggest best practices for SQLite integration. [Link](https://chatgpt.com/share/67bb324b-4ee8-8004-8c79-e12270be8a88)
