from product_manager import Product

def main():
    manager = Product()

    print("\nAdding Products...")
    manager.add_product("Laptop", 75000, "Electronics")
    manager.add_product("Table", 12000, "Furniture")
    manager.add_product("Smartphone", 50000, "Electronics")

    print("\nCalculating Total Value of Products in Stock...")
    total_value = manager.get_total_value()
    print(f"Total Value of Products: ₹{total_value}")

    manager.close_connection()

if __name__ == "__main__":
    main()
