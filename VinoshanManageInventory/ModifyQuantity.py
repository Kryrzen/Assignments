# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: ModifyQuantity.py
# Description:  Modifies the quantity of an existing record using a temporary file.

import os

def modify_record():
    original_file = 'coffee_inventory.txt'
    temp_file = 'temp_coffee_inventory.txt'
    
    # Stop if file does not exist
    if not os.path.exists(original_file):
        print("No inventory file found to modify.")
        return

    # Get search target and new data
    search_name = input("Enter the description of the coffee you want to modify: ").strip()
    new_quantity = input("Enter the new quantity: ").strip()
    
    found = False
    
    with open(original_file, 'r') as infile, open(temp_file, 'w') as outfile:
        while True:
            description = infile.readline()
            quantity = infile.readline()
            
            if not description:
                break
                
            desc_clean = description.strip()
            
            # Write new data if matched; copy old data if not
            if desc_clean.lower() == search_name.lower():
                outfile.write(f"{desc_clean}\n")
                outfile.write(f"{new_quantity}\n")
                found = True
            else:
                outfile.write(description)
                outfile.write(quantity)
                
    # Replace original file with temporary file if match was found
    if found:
        os.remove(original_file)
        os.rename(temp_file, original_file)
        print(f"Successfully updated quantity for '{search_name}'.\n")
    else:
        os.remove(temp_file)
        print(f"Could not find '{search_name}' in the inventory.\n")

if __name__ == "__main__":
    modify_record()