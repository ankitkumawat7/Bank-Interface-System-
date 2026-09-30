# Bank Interface System

import semi_file_1
import semi_file_2


def main():
    customers = semi_file_1.load_customers(semi_file_1.DEFAULT_STORAGE_PATH)

    while True:
        print("\nBank Interface System")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Remove Customer")
        print("4. Update Customer")
        print("5. Search Customer")
        print("6. Deposit Money")
        print("7. Withdraw Money")
        print("8. Exit")
        print("Type 'exit', 'quit', or 'q' at any prompt to cancel and return.")

        choice = input("Enter your choice: ").strip().lower()

        if choice in {'1', '2', '3', '4', '5', '6', '7', '8', '0', 'exit', 'quit', 'q'}:
            if choice in {'exit', 'quit', 'q', '0', '8'}:
                print("Exiting the system.")
                break
            if choice == '1':
                semi_file_1.add_customer(customers)
            elif choice == '2':
                semi_file_2.display_customers(customers)
            elif choice == '3':
                semi_file_1.remove_customer(customers)
            elif choice == '4':
                semi_file_2.update_customer(customers)
            elif choice == '5':
                semi_file_2.search_customer(customers)
            elif choice == '6':
                semi_file_2.deposit_money(customers)
            elif choice == '7':
                semi_file_2.withdraw_money(customers)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

