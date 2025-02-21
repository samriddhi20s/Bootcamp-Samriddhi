from inventory_manager import InventoryManager

def main():
    manager = InventoryManager()

    print("\nAdding Products...")
    manager.add_product("Laptop", 10)
    manager.add_product("Phone", 20)

    print("\nBefore Stock Update:")
    manager.fetch_inventory()

    print("\nUpdating Stock (Reduce 3 Laptops)...")
    manager.update_stock(1, -3)

    print("\nAfter Stock Update:")
    manager.fetch_inventory()

    print("\nInventory Log:")
    manager.fetch_logs()

    manager.close_connection()

if __name__ == "__main__":
    main()
