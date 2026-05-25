# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name:DisplayRecords.py
# Description: Reads and displays all current records from the inventory file.
import os

def display_inventory():
    print("=== Current Coffee Inventory ===")
    
    # Stop if file does not exist
    if not os.path.exists('coffee_inventory.txt'):
        print("No inventory file found. Add some records first!")
        return

    # Table formatting
    print(f"{'Coffee Description':<30} | {'Quantity':<10}")
    print("-" * 45)
    
    with open('coffee_inventory.txt', 'r') as file:
        while True:
            # Read a pair of lines
            description = file.readline()
            quantity = file.readline()
            
            # Break loop at end of file
            if not description:
                break
                
            # Clean and display data
            description = description.strip()
            quantity = quantity.strip()
            print(f"{description:<30} | {quantity:<10}")
            
    print("-" * 45 + "\n")

if __name__ == "__main__":
    display_inventory()