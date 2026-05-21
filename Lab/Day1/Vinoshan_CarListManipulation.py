# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_CarListManipulation.py
# Description: Create a list of cars and manipulate the list.

# Intialize the Car LIst
cars = ["Honda", "Toyota", "Mercedes", "Ferrari", "Nissan", "Hyundai"]

# Print List
for car in cars:
    print (car);
    
print("")
# Change Last Item to Kia
cars[5]= "Kia"

# Print List
for car in cars:
    print (car);
    
print("")
# Reverse the List
cars.reverse

# Print List
for car in cars:
    print (car);
    
print("")
# Empty all the members of the list
cars.clear();

# Print List
for car in cars:
    print (car);