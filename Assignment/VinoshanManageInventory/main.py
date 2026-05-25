# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: main.py
# Description: Dashboard to Control the Script

# Import functions from your existing scripts
from AddRecords import add_coffee_record
from DisplayRecords import display_inventory
from ModifyQuantity import modify_record

def main_menu():
    while True:
        print("COFFEE INVENTORY DASHBOARD")
        print("1. Add New Coffee Records")
        print("2. Display All Coffee Records")
        print("3. Modify a Record's Quantity")
        print("4. Exit Program")
        
        choice = input("Enter your choice (1-4): ").strip()
        print()
        
        if choice == '1':
            # Run AddRecords.py
            add_coffee_record()
        elif choice == '2':
            # Run DisplayRecords.py
            display_inventory()
        elif choice == '3':
            # Run ModifyQuantity.py 
            modify_record()
        elif choice == '4':
            print("Thank you for using the Coffee Inventory System. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number from 1 to 4.\n")

if __name__ == "__main__":
    main_menu()
