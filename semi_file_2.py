def display_customers(l):
    
    if len(l) == 1:
        print("No customers to display.")
        return
    
    for customer in l:
        print("Customer ID:", customer[0])
        print("Customer Name:", customer[1])
        print("Customer Address:", customer[2])
        print("Customer Phone:", customer[3])
        print("Customer Email:", customer[4])
        print("Account Number:", customer[5])
        print("Account Type:", customer[6])
        print("Account Balance:", customer[7])
        print("-----------------------------")
    
def update_customer(l):
    customer_id = input("Enter the customer ID to update: ")
    for customer in l:
        if customer[0] == customer_id:
            print("Updating details for customer ID:", customer_id)
            customer[1] = input("Enter new customer name: ")
            customer[2] = input("Enter new customer address: ")
            customer[3] = int(input("Enter new customer phone: "))
            customer[4] = input("Enter new customer email: ")
            customer[5] = input("Enter new account number: ")
            customer[6] = input("Enter new account type: ")
            customer[7] = float(input("Enter new account balance: "))
            print("Customer details updated successfully.")
            return
    print("No customer found with ID ", customer_id, ".")