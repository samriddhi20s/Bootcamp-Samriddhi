from order_manager import OrderManager

def main():
    manager = OrderManager()

    print("\nInserting Sample Data...")
    manager.insert_sample_data()

    print("\nBefore Update:")
    manager.fetch_orders()

    print("\nUpdating Orders in a Transaction...")
    manager.update_order_transaction(order_id=1, new_status="Shipped", product_name="Laptop", new_quantity=2, new_price=72000.00)

    print("\nAfter Update:")
    manager.fetch_orders()

    manager.close_connection()

if __name__ == "__main__":
    main()
