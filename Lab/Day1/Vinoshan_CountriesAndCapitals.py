# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_CountriesAndCapitals.py
# Description: This program uses dictionaries to define five countries and their
#              capitals, then prints based on their respective keys

# Intialize Dictionaries
country_capitals = {
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "United Kingdom": "London"
}

# Print Capitals of each country 
for country, capital in country_capitals.items():
    print(f"The capital of {country} is: {capital}")