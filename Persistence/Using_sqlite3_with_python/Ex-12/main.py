from product_manager import Product

def main():
    manager = Product()

    print("\nAdding Categories...")
    manager.add_category("Electronics")
    manager.add_category("Furniture")

    print("\nAdding Products...")
    manager.add_product("Laptop", 75000, "Electronics")
    manager.add_product("Table", 12000, "Furniture")
    manager.add_product("Smartphone", 50000, "Electronics")

    print("\nFetching Products with Categories...")
    products = manager.get_products_with_categories()

    if products:
        for p in products:
            print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]} | Category: {p[3]}")
    else:
        print("No products found.")

    manager.close_connection()

if __name__ == "__main__":
    main()
