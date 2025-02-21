from product_manager import Product

def main():
    manager = Product()

    while True:
        print("\n1. Add Product\n2. Update Product\n3. Delete Product\n4. List Products\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            manager.add_product(name, price)

        elif choice == "2":
            product_id = int(input("Enter product ID to update: "))
            new_price = float(input("Enter new price: "))
            manager.update_product(product_id, new_price)

        elif choice == "3":
            product_id = int(input("Enter product ID to delete: "))
            manager.delete_product(product_id)

        elif choice == "4":
            manager.list_products()

        elif choice == "5":
            print("Exiting program.")
            manager.close_connection()
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
