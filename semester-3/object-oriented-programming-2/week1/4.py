
"""
This program will caclculate the inputs from users to figure out the total of a customers rentals for both old and new movies

will take inputs for old and new movies and multiply it by their rates

will then add those together and multiply by sales tax as well at outputting the total
"""

#MOVIES INPUTS   
new_movies_amount = int(input("Enter the number of NEW movies rented: ")) * 3.00#prompts and asks for a number and only allows int. then it multiplies it by 3 because thats the rates for new movies
old_movies_amount = int(input("Enter the number of OLD movies rented: ")) * 2.00#prompts and asks for a number but only accepts int. then it multiplies it by 2 because thats the rates for old movies

#TOTAL
total = (new_movies_amount + old_movies_amount) * 1.05#adds the old and new movies amounts together and then multiplies it by the wisconsin sales tax

#END
print(f"Total charge is {total:.2f}")#outputs the total and makes sure its only has 2 decimal places