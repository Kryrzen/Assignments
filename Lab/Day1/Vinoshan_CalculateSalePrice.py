# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_CalculateSalePrice.py
# Description: Calculates a 20% discount on an item's original price and
#          displays the final sale price.

# Define the discount percentage as a constant (20%)
DISCOUNT_RATE = 0.20

# Prompt the user to enter the price
item_price = float(input("Enter the price of the item: $"))

# Calculate the discount amount
discount_amount = item_price * DISCOUNT_RATE

# Calculate the final sale price
sale_price = item_price - discount_amount

# Display the final sale price
print(f"The sale price after a 20% discount is ${sale_price:.2f}")