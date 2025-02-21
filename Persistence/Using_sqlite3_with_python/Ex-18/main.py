from product_manager import ProductManager

def main():
    manager = ProductManager()

    print("\nInserting Batch Data...")
    products = [
        ("Laptop", 75000.00),
        ("Mouse", 1500.00),
        ("Keyboard", 2500.00),
        ("Monitor", 12000.00),
        ("Phone", 50000.00)
    ]
    manager.batch_insert_products(products)

    print("\nFetching Products:")
    manager.fetch_products()

    manager.close_connection()

if __name__ == "__main__":
    main()
