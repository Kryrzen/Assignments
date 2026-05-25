# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_CountriesAndCapitals.py
# Description: Create Two Sets: One for baseball team and other for
#              basketball team. Perform various set operation to 
#              analyze the membership of the students.

#Intialize Basketball Team
basketball_team = {"Jack", "Jess", "Jane", "Jen", "Juliet", "Jap"}

#Intialize Baseball Team
baseball_team = {"Jack", "Jane", "Juliet", "Jacob", "Jax", "Justice"}

#Find the intersection of the sets to display the names of students who play both sports.
print("Intersection: ",  baseball_team.intersection(basketball_team))

#Find the union of the sets to display the names of students who play either sport.
print("Union: ", basketball_team.union(baseball_team))

'''Find the difference of the baseball and basketball sets to display the names 
 of students who play baseball but not basketball'''
print("Difference(baseball): ", baseball_team.difference(basketball_team))

'''Find the difference of the basketball and baseball sets 
to display the names of students who play basketball but not baseball. '''
print("Difference(basketball): ", basketball_team.difference(baseball_team))

'''Find the symmetric difference of the basketball and baseball sets to 
display the names of students who play one sport but not both. '''
print("Symmetric Difference: ", basketball_team.symmetric_difference(baseball_team))


print("Number\tSquare")
print("-------------------")

for number in range(1, 11):   # Displays numbers 1 through 10
    square = number ** 2
    print(f"{number}\t{square}")
