from product_manager import Product

def main():
    manager = Product()

    if not manager.check_data_exists():
        print("No products found in the database. Adding sample data...")
        manager.insert_sample_data()

    name_fragment = input("Enter product name to search: ")
    products = manager.search_product(name_fragment)

    if products:
        for p in products:
            print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]}")
    else:
        print(f"No products found matching '{name_fragment}'.")

    manager.close_connection()

if __name__ == "__main__":
    main()
