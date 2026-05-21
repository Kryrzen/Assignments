# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_FormatFInancialInfo.py
# Description: This program cleanly formats and displays financial metrics using 
#              proper comma placement separators and explicit currency precision.

#Initialize financial variables
quantity = 10000
total = 1507500
price = 150.75

# Format and display the information 
print(f"It cost me ${total:,} to buy {quantity:,} quantity of office supplies at the Ottawa Campus.")
print(f"The individual price of the item was ${price:,.2f}.")