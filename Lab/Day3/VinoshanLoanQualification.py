# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanLoanQualification.py
# Description: User enters Income, How long they were employed and 
# Credit score to see if they qualify for a loan.

#Check if user can get a loan
def qualify_loan(income, employed, creditscore):
    #if user meets requirements, they quaify for a loan
    if (income >= 30000 and employed >= 2 and creditscore >= 600):
        print("\nCongratulations! You Qualify for a Loan!")
    #dont qualify a loan    
    else:
        print("\nUnfortunately you do not Qualify")

def main():
    #Get user inputs
    income = float(input("Enter How much you Earn: "))
    employed = float(input("Enter How long you worked for: "))
    creditscore = float(input("Enter your credit score: "))

    qualify_loan(income, employed, creditscore)

main()