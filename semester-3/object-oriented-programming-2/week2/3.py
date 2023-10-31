# page 100 problem 7

# function to get positive valid integer
def input_valid_positive_integer(input_string: str):
    user_input = -1
    while True:
        try:
            user_input = int(input(input_string))
            if user_input > 0:
                return user_input
            print("Enter a positive number")
        except ValueError:
            print("Invalid entry, try again")

# function to get valid positive float
def input_valid_positive_float(input_string: str):
    user_input = -1
    while True:
        try:
            user_input = float(input(input_string))
            if user_input > 0:
                return user_input
            print("Enter a positive number")
        except ValueError:
            print("Invalid entry, try again")

# function to calculate the salary
def calculate_salary(starting_salary: float, percentage_increase: float, years: int):
    salary_schedule = []

    current_salary = starting_salary
    for year in range(1, years + 1):
        salary_schedule.append((year, current_salary))
        current_salary += current_salary * (percentage_increase / 100)

    return salary_schedule
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~










# tries getting inputs
starting_salary = input_valid_positive_float("Enter the starting salary: $")
percentage_increase = input_valid_positive_float("Enter the percantage increase (2 for 2%): ")
years = input_valid_positive_integer("Enter the number of years in the schedule: ")

# does the math stuff
salary_schedule = calculate_salary(starting_salary, percentage_increase, years)

# final output
print("Year\tSalary")
for year, salary in salary_schedule:
    print(f"{year}\t${salary:.2f}")