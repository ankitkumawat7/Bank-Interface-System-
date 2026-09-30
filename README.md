# Bank Interface System

A Python command-line banking management project for handling customer records, basic account operations, and persistent storage in JSON files.

## Features

- Add new customers
- Display all customer records
- Remove a customer by ID
- Update customer details
- Search a customer by ID
- Deposit money
- Withdraw money
- Safe exit commands using `exit`, `quit`, `q`, or option `8`
- Persistent storage in a `customer_data` folder
- Each customer is saved as a separate JSON file
- A central index file keeps track of saved customers

## Project structure

- `#bank interface system.py` – main menu and program flow
- `semi_file_1.py` – customer creation, validation, storage, and persistence logic
- `semi_file_2.py` – display/search/deposit/withdraw helpers
- `test_bank_system.py` – automated regression tests
- `customer_data/` – saved customer JSON files

## How to run

```bash
cd "/workspaces/Bank-Interface-System-"
python3 "./#bank interface system.py"
```

## Example menu

```text
Bank Interface System
1. Add Customer
2. Display Customers
3. Remove Customer
4. Update Customer
5. Search Customer
6. Deposit Money
7. Withdraw Money
8. Exit
```

## JSON storage format

Customer data is saved separately using the customer ID as the file name. For example:

- `customer_data/C001.json`
- `customer_data/customers.json`

This keeps each customer record individual and allows data to be loaded back when the program starts.

## Validation

The system checks for:

- duplicate customer IDs
- invalid phone numbers
- invalid numeric balances
- negative or zero deposit/withdrawal values
- invalid menu choices

## Test status

The project includes automated tests and currently passes:

```bash
pytest -q
```
