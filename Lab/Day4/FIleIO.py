# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: FIleIO.py
# Description: Function that accepts the file name as a parameter, 
#              reads the file line by line, and stores each line into a list. 
#              Uses car.txt file, calls the function and pass the file to 
#              function and print the created list.

# Reads the file and make the a new list
def read_file_into_list(filename):
    lines_list = []

    # Read File line by line and append to lines_list
    with open(filename, "r") as file:
        for line in file:
            lines_list.append(line.strip())

    # returns lines_list
    return lines_list


def main():
    # File Name 
    filename = "cars.txt" 
    #Sends in File to function
    car_list = read_file_into_list(filename)

    # Display Output
    print("List created from file: \n",car_list)

main()
