# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanLoanQualification.py
# Description: Determine if a customer qualifies for a loan based on their annual income 
# and years of employment.

#Get User Input
YEARSEMPLOYED = int(input("Enter how long you were employed: "))
INCOME = float(input("Enter Income: "))

#Logic: When Both Criteria are met, you are approved. Else you are Denied
if YEARSEMPLOYED >= 2 and INCOME >= 30000.00:
    print("You are approved for the loan.")
else:
    print("You are denied for the loan.")