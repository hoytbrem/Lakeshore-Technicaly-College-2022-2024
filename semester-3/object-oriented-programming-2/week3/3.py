"""
12. The Payroll Department keeps a list of employee information for each pay period
in a text file. The format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Write a program that inputs a filename from the user and prints to the terminal a
report of the wages paid to the employees for the given period. The report should
be in tabular format with the appropriate header. Each line should contain an
employee's name, the hours worked, and the wages paid for that period
"""

# Prompt the user to enter the input file name
file = input("Input file name: ")

# Open the file for reading using a context manager (with statement)
with open(file, "r") as f:
    # Print the header for the report
    print("Employee Name\tHours Worked\tWages Paid")

    # Process each line in the file
    for line in f:
        # Split the line into components (split by whitespace)
        components = line.split()

        # Check if there are at least 3 components to form a valid record
        if len(components) >= 3:
            # Extract components from the split line
            last_name = components[0]
            hourly_wage = float(components[1])
            hours_worked = float(components[2])

            # Calculate wages paid for the employee
            wages_paid = hourly_wage * hours_worked

            # Print the report for this employee in tabular format
            print(f"{last_name}\t\t{hours_worked}\t\t{wages_paid:.2f}")
        else:
            # Print an error message for an invalid record
            print(f"Invalid record: {line.strip()}")
