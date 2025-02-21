from customer_manager import CustomerManager

def main():
    manager = CustomerManager()

    print("\nInserting Customers in a Transaction...")
    customers_list = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Davis", "charlie@example.com")
    ]
    
    manager.insert_customers(customers_list)

    print("\nFetching All Customers...")
    manager.fetch_all_customers()

    manager.close_connection()

if __name__ == "__main__":
    main()
