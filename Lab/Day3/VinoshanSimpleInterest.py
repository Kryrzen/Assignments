# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanSimpleInterest.py
# Description: Calculate interest for a client using two functions. Client enters 3 values.

# Function to calculate and display simple interest
def show_interest_function(principal, rate, periods):
    #Converts Rate in %
    rate /= 100
    #Calculates Interest
    simple_interest = principal * rate * periods
    #Displays Interest
    print(f"\nSimple Interest: ${simple_interest:.2f}")

# Main function to get user input
def main():
    #User Input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    periods = float(input("Enter the number of periods: "))

    #Calls functions and sends in the user inputs
    show_interest_function(principal, rate, periods)

main()
