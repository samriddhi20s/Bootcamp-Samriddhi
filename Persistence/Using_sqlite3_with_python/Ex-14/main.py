from product_manager import Product

def main():
    manager = Product()

    print("\nAdding Products...")
    manager.add_product("Laptop", 75000, "Electronics")
    manager.add_product("Table", 12000, "Furniture")
    manager.add_product("Smartphone", 50000, "Electronics")

    print("\nExporting Products to CSV...")
    manager.export_to_csv()

    manager.close_connection()

if __name__ == "__main__":
    main()
