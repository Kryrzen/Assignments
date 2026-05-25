# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: pandaex.py
# Description: Exercise for Panada

import pandas as pd
import numpy as np
import random

# Creating a Series
s = pd.Series([1, 3, 5, 7, 9])
sd = s

# Accessing elements in a Series
print(s[0])  # Accessing the first element
print(s[1:4])  # Accessing a range of elements
print()

# Basic Operations on Series
print(s + 2)
print()

# Filtering Data
filtered_s = s[s > 5]
print(filtered_s)
print()

# Calculating Statistics
print(sd.mean())  # Mean of the Series
print(sd.median())  # Median of the Series
print(sd.std())  # Standard Deviation of the Series
print()

# Complete the below python program to convert the dictionary to dataframe
np.random.seed()

# Create a DataFrame with randomly generated data
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": np.random.randint(20, 70, size=5),
    "salary": np.random.randint(30000, 90000, size=5),
}
# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# save the dataframe to csv file
df.to_csv("employee_data.csv", index=False)

print()
