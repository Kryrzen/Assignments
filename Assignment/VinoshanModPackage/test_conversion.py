# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: test_conversion.py
# Description: A package for converting temperature and distance units.


import unitconvert as uc

def main():
    # Fahrenheit to Celsius
    f_temp = 98.6
    c_temp = uc.fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is equal to {c_temp:.2f}°C")
    
    # Celsius to Fahrenheit
    c_temp_input = 25
    f_temp_output = uc.celsius_to_fahrenheit(c_temp_input)
    print(f"{c_temp_input}°C is equal to {f_temp_output:.2f}°F")

    # MIles to Kilometers
    miles = 10
    km = uc.miles_to_kilometers(miles)
    print(f"{miles} miles is equal to {km:.2f} km")
    
    # Kilometers to Miles
    kilometers = 10
    mi = uc.kilometers_to_miles(kilometers)
    print(f"{kilometers} km is equal to {mi:.2f} miles")

if __name__ == "__main__":
    main()