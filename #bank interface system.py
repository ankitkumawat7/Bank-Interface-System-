#bank interface system

import semi_file_1
import semi_file_2



def main(l):
    while True:
        print("Bank Interface System")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Remove Customer")
        print("4. Update Customer")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            semi_file_1.add_customer(l)
        elif choice == '2':
            semi_file_2.display_customers(l)
        elif choice == '3':
            semi_file_1.remove_customer(l)
        elif choice == '4':
            semi_file_2.update_customer(l)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
  
  
l=["customer_id","customer_name","customer_address","customer_phone","customer_email","account_number","account_type","account_balance"]            
if __name__ == "__main__":
    main(l)




