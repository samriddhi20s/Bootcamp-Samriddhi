from product_manager import Product

def main():
    manager = Product()

    print("\nBatch Inserting Products...")
    products_list = [
        ("Smart TV", 55000, "Electronics"),
        ("Chair", 8000, "Furniture"),
        ("Headphones", 3000, "Electronics"),
        ("Coffee Table", 15000, "Furniture"),
        ("Keyboard", 2000, "Accessories")
    ]
    manager.add_products_batch(products_list)

    print("\nFetching All Products...")
    manager.fetch_all_products()

    manager.close_connection()

if __name__ == "__main__":
    main()
