import semi_file_1


def display_customers(l):
    semi_file_1.display_customers(l)


def update_customer(l):
    return semi_file_1.update_customer(l)


def search_customer(l):
    customer_id = input("Enter the customer ID to search: ").strip()
    if semi_file_1.should_exit(customer_id):
        print("Search cancelled.")
        return
    for customer in semi_file_1._normalize_customers(l):
        if customer.get("customer_id") == customer_id:
            print("Customer found:")
            print(customer)
            return
    print(f"No customer found with ID {customer_id}.")


def deposit_money(l):
    customer_id = input("Enter the customer ID: ").strip()
    if semi_file_1.should_exit(customer_id):
        print("Deposit cancelled.")
        return
    for customer in semi_file_1._normalize_customers(l):
        if customer.get("customer_id") == customer_id:
            while True:
                amount_input = input("Enter amount to deposit: ").strip()
                if semi_file_1.should_exit(amount_input):
                    print("Deposit cancelled.")
                    return
                try:
                    amount = float(amount_input)
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Deposit amount must be a positive number.")

            customer["account_balance"] = customer.get("account_balance", 0.0) + amount
            semi_file_1.save_customers(l, semi_file_1.DEFAULT_STORAGE_PATH)
            print(f"Deposit successful. New balance: {customer['account_balance']}")
            return
    print(f"No customer found with ID {customer_id}.")


def withdraw_money(l):
    customer_id = input("Enter the customer ID: ").strip()
    if semi_file_1.should_exit(customer_id):
        print("Withdrawal cancelled.")
        return
    for customer in semi_file_1._normalize_customers(l):
        if customer.get("customer_id") == customer_id:
            while True:
                amount_input = input("Enter amount to withdraw: ").strip()
                if semi_file_1.should_exit(amount_input):
                    print("Withdrawal cancelled.")
                    return
                try:
                    amount = float(amount_input)
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Withdrawal amount must be a positive number.")

            if amount > customer.get("account_balance", 0.0):
                print("Insufficient balance for this withdrawal.")
                return

            customer["account_balance"] = customer.get("account_balance", 0.0) - amount
            semi_file_1.save_customers(l, semi_file_1.DEFAULT_STORAGE_PATH)
            print(f"Withdrawal successful. New balance: {customer['account_balance']}")
            return
    print(f"No customer found with ID {customer_id}.")
