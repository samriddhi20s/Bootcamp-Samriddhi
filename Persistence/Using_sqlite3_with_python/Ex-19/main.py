from banking_manager import BankingManager

def main():
    manager = BankingManager()

    print("\nCreating Initial Accounts...")
    manager.create_accounts()

    print("\nBefore Transaction:")
    manager.fetch_accounts()

    print("\nTransferring ₹2000 from Alice (1) to Bob (2)...")
    manager.transfer_funds(1, 2, 2000)

    print("\nAfter Transaction:")
    manager.fetch_accounts()

    manager.close_connection()

if __name__ == "__main__":
    main()
