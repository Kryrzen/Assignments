# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanPrintIntegers.py
# Description: Given a List, figure out which index of a list is an Integer.
#              Determine the Sum and Average of the Given List

#Given List
my_list = [10, 'a', 'z', -15.0, 8.00, 'h', 9.00, 80, 'q', 'r', 's', 4, 200, -8.00]

#Intialize Variable
int_list = []
sum = 0

# Logic
for item in my_list:
    #Check if item in list is int and adds to int_list
    if type(item) == int:
        int_list.append(item)
        #Adds item into sum to calculate total of all integers
        sum += item

# Displays int_list
print ("List", int_list)
# Displays total
print("Total:", sum)
# Displays Average
print ("Average: ", sum / len(int_list))