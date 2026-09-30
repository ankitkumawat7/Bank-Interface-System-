import json
import os


CUSTOMER_FIELDS = [
    "customer_id",
    "customer_name",
    "customer_address",
    "customer_phone",
    "customer_email",
    "account_number",
    "account_type",
    "account_balance",
]

DEFAULT_STORAGE_PATH = os.path.join(os.getcwd(), "customer_data")


def should_exit(value):
    return str(value).strip().lower() in {"exit", "quit", "q", "cancel", "close", "0"}


def save_customers(customers, storage_dir=DEFAULT_STORAGE_PATH):
    os.makedirs(storage_dir, exist_ok=True)
    index = []

    for customer in customers:
        if not isinstance(customer, dict):
            continue

        customer_id = str(customer.get("customer_id", "")).strip()
        if not customer_id:
            continue

        file_path = os.path.join(storage_dir, f"{customer_id}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(customer, file, indent=2)

        index.append({
            "customer_id": customer_id,
            "file": f"{customer_id}.json",
        })

    index_path = os.path.join(storage_dir, "customers.json")
    with open(index_path, "w", encoding="utf-8") as file:
        json.dump(index, file, indent=2)

    return index_path


def load_customers(storage_dir=DEFAULT_STORAGE_PATH):
    index_path = os.path.join(storage_dir, "customers.json")
    if not os.path.exists(index_path):
        return []

    try:
        with open(index_path, "r", encoding="utf-8") as file:
            index = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    customers = []
    for item in index:
        customer_id = str(item.get("customer_id", "")).strip()
        if not customer_id:
            continue
        file_name = item.get("file", f"{customer_id}.json")
        file_path = os.path.join(storage_dir, file_name)
        if not os.path.exists(file_path):
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                customer = json.load(file)
            if isinstance(customer, dict):
                customers.append(customer)
        except (json.JSONDecodeError, OSError):
            continue

    return customers


def _normalize_customers(customers):
    if not customers:
        return []

    normalized = []
    working_list = list(customers)

    if working_list and isinstance(working_list[0], str):
        working_list = working_list[1:]

    for item in working_list:
        if isinstance(item, dict):
            normalized.append(item)
        elif isinstance(item, list) and len(item) == len(CUSTOMER_FIELDS):
            normalized.append(dict(zip(CUSTOMER_FIELDS, item)))

    return normalized


def add_customer(l):
    customers = _normalize_customers(l)

    count_input = input("Enter the number of customers to add: ").strip()
    if should_exit(count_input):
        print("Customer addition cancelled.")
        return l

    try:
        n = int(count_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return l

    if n < 0:
        print("Number of customers cannot be negative.")
        return l

    for _ in range(n):
        customer = {}

        while True:
            customer_id = input("Enter customer id: ").strip()
            if should_exit(customer_id):
                print("Customer addition cancelled.")
                return l
            if customer_id and not any(c.get("customer_id") == customer_id for c in customers):
                customer["customer_id"] = customer_id
                break
            if not customer_id:
                print("Customer ID cannot be empty.")
            else:
                print("Customer ID already exists. Please enter a unique ID.")

        customer_name = input("Enter customer name: ").strip()
        if should_exit(customer_name):
            print("Customer addition cancelled.")
            return l
        customer["customer_name"] = customer_name

        customer_address = input("Enter customer address: ").strip()
        if should_exit(customer_address):
            print("Customer addition cancelled.")
            return l
        customer["customer_address"] = customer_address

        while True:
            phone_input = input("Enter customer phone: ").strip()
            if should_exit(phone_input):
                print("Customer addition cancelled.")
                return l
            try:
                customer["customer_phone"] = int(phone_input)
                break
            except ValueError:
                print("Phone number must be a valid integer.")

        customer_email = input("Enter customer email: ").strip()
        if should_exit(customer_email):
            print("Customer addition cancelled.")
            return l
        customer["customer_email"] = customer_email

        account_number = input("Enter account number: ").strip()
        if should_exit(account_number):
            print("Customer addition cancelled.")
            return l
        customer["account_number"] = account_number

        account_type = input("Enter account type: ").strip()
        if should_exit(account_type):
            print("Customer addition cancelled.")
            return l
        customer["account_type"] = account_type

        while True:
            balance_input = input("Enter account balance: ").strip()
            if should_exit(balance_input):
                print("Customer addition cancelled.")
                return l
            try:
                customer["account_balance"] = float(balance_input)
                break
            except ValueError:
                print("Account balance must be a valid number.")

        customers.append(customer)

    l[:] = customers
    save_customers(customers, DEFAULT_STORAGE_PATH)
    return l


def remove_customer(l):
    customers = _normalize_customers(l)
    customer_id = input("Enter the customer ID to remove: ").strip()
    if should_exit(customer_id):
        print("Removal cancelled.")
        return l

    for customer in customers:
        if customer.get("customer_id") == customer_id:
            customers.remove(customer)
            l[:] = customers
            save_customers(customers, DEFAULT_STORAGE_PATH)
            print(f"Customer with ID {customer_id} has been removed.")
            return l

    print(f"No customer found with ID {customer_id}.")
    l[:] = customers
    save_customers(customers, DEFAULT_STORAGE_PATH)
    return l


def display_customers(l):
    customers = _normalize_customers(l)

    if not customers:
        print("No customers to display.")
        return

    for customer in customers:
        print("Customer ID:", customer.get("customer_id"))
        print("Customer Name:", customer.get("customer_name"))
        print("Customer Address:", customer.get("customer_address"))
        print("Customer Phone:", customer.get("customer_phone"))
        print("Customer Email:", customer.get("customer_email"))
        print("Account Number:", customer.get("account_number"))
        print("Account Type:", customer.get("account_type"))
        print("Account Balance:", customer.get("account_balance"))
        print("-----------------------------")


def update_customer(l):
    customers = _normalize_customers(l)
    customer_id = input("Enter the customer ID to update: ").strip()
    if should_exit(customer_id):
        print("Update cancelled.")
        return l

    for customer in customers:
        if customer.get("customer_id") == customer_id:
            print("Updating details for customer ID:", customer_id)

            new_name = input("Enter new customer name: ").strip()
            if should_exit(new_name):
                print("Update cancelled.")
                return l
            customer["customer_name"] = new_name

            new_address = input("Enter new customer address: ").strip()
            if should_exit(new_address):
                print("Update cancelled.")
                return l
            customer["customer_address"] = new_address

            while True:
                phone_input = input("Enter new customer phone: ").strip()
                if should_exit(phone_input):
                    print("Update cancelled.")
                    return l
                try:
                    customer["customer_phone"] = int(phone_input)
                    break
                except ValueError:
                    print("Phone number must be a valid integer.")

            new_email = input("Enter new customer email: ").strip()
            if should_exit(new_email):
                print("Update cancelled.")
                return l
            customer["customer_email"] = new_email

            new_account_number = input("Enter new account number: ").strip()
            if should_exit(new_account_number):
                print("Update cancelled.")
                return l
            customer["account_number"] = new_account_number

            new_account_type = input("Enter new account type: ").strip()
            if should_exit(new_account_type):
                print("Update cancelled.")
                return l
            customer["account_type"] = new_account_type

            while True:
                balance_input = input("Enter new account balance: ").strip()
                if should_exit(balance_input):
                    print("Update cancelled.")
                    return l
                try:
                    customer["account_balance"] = float(balance_input)
                    break
                except ValueError:
                    print("Account balance must be a valid number.")

            l[:] = customers
            save_customers(customers, DEFAULT_STORAGE_PATH)
            print("Customer details updated successfully.")
            return l

    print(f"No customer found with ID {customer_id}.")
    l[:] = customers
    save_customers(customers, DEFAULT_STORAGE_PATH)
    return l
