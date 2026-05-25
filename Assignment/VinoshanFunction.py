# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanFunction.py
# Description: User enters a string and calculates the number of lowercase and uppercase letters.

# Function to Count Letters
def count_letters(user_text):

    #intialize variables
    lowercase_count = 0
    uppercase_count = 0

    for char in user_text:
        #Adds 1 if Lowercase
        if char.islower():
            lowercase_count += 1
        #Adds 1 if Uppercase    
        elif char.isupper():
            uppercase_count += 1

    print(f"\nTotal lowercase letters: {lowercase_count}")
    print(f"Total uppercase letters: {uppercase_count}")


def main():
    #User Enters a String
    text = input("Enter a string: ")
    count_letters(text)


main()
