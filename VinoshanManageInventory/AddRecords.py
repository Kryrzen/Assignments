# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: AddRecords.py
# Description: Appends new coffee descriptions and quantities to the inventory file.

import os

def add_coffee_record():
    print("--- Add Coffee to Inventory ---")
    
    # Get user inputs
    description = input("Enter coffee description: ").strip()
    quantity = input("Enter quantity: ").strip()
    
    filename = 'coffee_inventory.txt'
    needs_newline = False
    
    # Check if file exists and has content
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            content = file.read()
            # If the file doesn't end with a newline character, we need to add one
            if not content.endswith('\n'):
                needs_newline = True

    # Open file in append mode and write data safely
    with open(filename, 'a') as file:
        if needs_newline:
            file.write('\n')
        file.write(f"{description}\n")
        file.write(f"{quantity}\n")
        
    print(f"Successfully added {description} to inventory!\n")

if __name__ == "__main__":
    while True:
        add_coffee_record()