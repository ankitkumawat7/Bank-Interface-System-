# Bank Interface System - Project Report

## Overview
This project is a Python-based command-line banking application that manages customer information and account operations. It provides a menu-driven interface for adding, displaying, updating, removing, searching, depositing, and withdrawing funds.

The application also stores customer records persistently in JSON files so the data remains available even after the program exits.

## Key Features

### 1. Customer Management
The system allows the user to manage customer records through a simple menu interface.

- Add a customer
- Display all customers
- Remove a customer by ID
- Update customer details

This makes the application useful for basic bank record management.

### 2. Search Functionality
Users can search for a customer by their unique customer ID.

This is useful for quickly locating a specific account or customer profile without browsing through all records manually.

### 3. Deposit and Withdrawal Features
The system supports core account actions:

- Deposit money into an account
- Withdraw money from an account
- Prevent invalid transactions such as negative values or withdrawals above available balance

This gives the project more realistic banking behavior beyond just data entry.

### 4. Exit and Cancel Options
The program includes clear exit support using commands such as:

- `8`
- `exit`
- `quit`
- `q`

This is helpful because users can leave the program cleanly or cancel at any prompt without confusing loops or repeated errors.

### 5. JSON Persistence
The application stores customer data in a dedicated `customer_data` folder.

Each customer is saved in its own JSON file, and a central index file is maintained to keep track of the records. This means data is preserved across program runs.

Example files:

- `customer_data/customers.json`
- `customer_data/C001.json`

This gives the project a simple but effective persistence layer without requiring a database.

## Screenshot-Based Observations

### Screenshot 1: Project files and README
The repository includes the main Python files, JSON data folder, tests, and documentation.

This shows a complete mini project structure with a working application and supporting files.

### Screenshot 2: Menu screen
The application presents a menu with the following operations:

1. Add Customer
2. Display Customers
3. Remove Customer
4. Update Customer
5. Search Customer
6. Deposit Money
7. Withdraw Money
8. Exit

This confirms the system is menu-driven and easy to use from the terminal.

### Screenshot 3: Withdrawal example
The program successfully accepts input for a customer ID and amount, then performs a withdrawal.

Example output shown in the screenshot:

- Enter the customer ID: C001
- Enter amount to withdraw: 6969
- Withdrawal successful. New balance: 2649.75

This demonstrates that the account balance update logic works correctly.

### Screenshot 4: Exit behavior
The menu includes the following message:

> Type 'exit', 'quit', or 'q' at any prompt to cancel and return.

This confirms the exit and cancel functionality was added to reduce stuck flows and improve usability.

## Validation and Quality Checks
The project includes automated tests in `test_bank_system.py`, which verify:

- customer creation
- update behavior
- removal behavior
- exit command behavior
- JSON persistence

These tests ensure the system behaves as expected and reduces the chance of regression bugs.

## Conclusion
The Bank Interface System is a functional command-line banking project that includes customer management, account transaction support, safe exit handling, and JSON-based persistence. The screenshots demonstrate that the system works in practice and that the features are accessible in a real terminal environment.

This project is a strong beginner-to-intermediate Python banking application with solid menu logic, validation, and persistent storage.
