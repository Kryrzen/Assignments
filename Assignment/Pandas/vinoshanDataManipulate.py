# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: vinoshanDataManipulate.py
# Description: Takes a CSV file then calculate and inserts the following entities as columns to your DataFrame.

import pandas as pd

# Read the CSV file into a DataFrame
assignmentcsv = pd.read_csv("Assignment.csv")
# Rename the first column to "Country"
assignmentcsv = assignmentcsv.rename(columns={"Unnamed: 0": "Country"})

# Calculate new columns
assignmentcsv["Total Games"] = (
    assignmentcsv["Summer_Game"] + assignmentcsv["Winter_Games"]
)

# Calculate the combined total of medals for each type
assignmentcsv["Gold_Combined_Total"] = assignmentcsv["Gold"] + assignmentcsv["Gold.1"]
assignmentcsv["Silver_Combined_Total"] = (
    assignmentcsv["Silver"] + assignmentcsv["Silver.1"]
)
assignmentcsv["Bronze_Combined_Total"] = (
    assignmentcsv["Bronze"] + assignmentcsv["Bronze.1"]
)

# Calculate the combined total of medals
assignmentcsv["Combined total"] = (
    assignmentcsv["Gold_Combined_Total"]
    + assignmentcsv["Silver_Combined_Total"]
    + assignmentcsv["Bronze_Combined_Total"]
)

# Show result and shows no index
print(assignmentcsv.to_string(index=False))
