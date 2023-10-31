"""
This program is designed to help users calculate how much money the make each week

it starts by taking the inputs for their hourly wage and then will ask how many hours they worked on overtime and not on overtime

it will then do the math and create an output for the user
"""

#TAKES ALL THE INPUTS
hourly_wage = float(input("Enter your hourly wage: "))#asks user for hourly wage but makes sure that it is a float
non_overtime_hours = float(input("Enter NONE OVERTIME hours worked this week: "))#asks user for non overtime hours and makes it a float
overtime_hours = float(input("Enter OVERTIME hours worked this week: "))#asks user for overtime hours and makes it a float

#DOES INTERNAL MATH
total = (hourly_wage * non_overtime_hours) + (hourly_wage * overtime_hours * 1.5)#finds how much they made during non overtime and during overtime and adds them together
total = total - (total * 0.0350)#takes the total and subtracts the income tax

#OUTPUTS
print(f"Your weekly total is: {total:.2f}")#will print their total and make sure that it is only to 2 decimal places