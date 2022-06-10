from dataclasses import replace


# name = input("Enter your name\n")
# print("Good Afternoon, " + name)
# Python program to get
# current date
  
  
# Import date class from datetime module
from datetime import date
from time import strptime, time
  
  
# Returns the current local date
today = date.today()
b=str(today)
# today = time.today()
# b=str(today)

a = input("Enter your name\n")


letter ='''
Dear <name> 
       you are selected for an interview
       
       congratulations <name>
       Date <current>
'''

letter = letter.replace("<name>",a)
letter = letter.replace("<current>",b)

print(letter)