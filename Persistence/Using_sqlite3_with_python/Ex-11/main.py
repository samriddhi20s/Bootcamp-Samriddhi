from product_manager import Product

def main():
    manager = Product()

    # Adding a product inside a transaction
    print("\nAdding Products...")
    manager.add_product("Laptop", 75000)
    manager.add_product("Phone", 40000)
    manager.add_product("", 5000)  # Invalid: Should be rolled back

    # Updating a product price inside a transaction
    print("\nUpdating Product Price...")
    manager.update_price(1, 72000)  # ✅ Valid
    manager.update_price(2, -5000)  # ❌ Invalid: Should be rolled back

    # Deleting a product inside a transaction
    print("\nDeleting Product...")
    manager.delete_product(2)  # ✅ Valid delete operation

    # Searching for products
    print("\nSearching for Products...")
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
