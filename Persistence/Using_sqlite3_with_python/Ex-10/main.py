from product_manager import Product

def main():
    manager = Product()

    # Test cases for validation
    try:
        manager.add_product("Phone", 30000)  # Valid
        manager.add_product("", 20000)       # Invalid name
        manager.add_product("Tablet", -5000) # Invalid price
    except Exception as e:
        print(f"Validation Error: {e}")

    # Search for products to check insertion
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
