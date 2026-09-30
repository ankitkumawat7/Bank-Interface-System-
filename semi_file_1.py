def add_customer(l):
    try:
        n=int(input("Enter the number of customers to add: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        add_customer(l)
        
    for i in range(n):
        customer = []
        for field in l:
            
            customer_id = input("enter customer id: ")
            customer_name = input("enter customer name: ")
            customer_address = input("enter customer address: ")
            customer_phone = int(input("enter customer phone: "))
            customer_email = input("enter customer email: ")
            account_number = input("enter account number: ")
            account_type = input("enter account type: ")
            account_balance = float(input("enter account balance: "))
            
            customer=[customer_id, customer_name, customer_address, customer_phone, customer_email, account_number, account_type, account_balance]
            l.append(customer)
            
    return l

def remove_customer(l):
    customer_id = input("Enter the customer ID to remove: ")
    for customer in l:
        if customer[0] == customer_id:
            l.remove(customer)
            print("Customer with ID ", customer_id, " has been removed.")
            return
    print("No customer found with ID ", customer_id, ".")