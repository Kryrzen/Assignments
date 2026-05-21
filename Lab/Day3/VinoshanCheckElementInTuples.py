# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanCheckElementInTuples.py
# Description: Ask the user to input a color and achecks if 
#              the specified color exists in the tuples of tuples.

# Define the tuple of tuples
tuple_of_tuples = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

# Ask user for a color
user_color = input("Enter a color: ")

# Logic
found = False
for group in tuple_of_tuples:
    if user_color.capitalize() in group:
        found = True
        break

# Display result
if found:
    print(f"{user_color} exists in the tuple.")
else:
    print(f"{user_color} does not exist in the tuple.")