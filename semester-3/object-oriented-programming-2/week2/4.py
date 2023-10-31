# page 101 problem 9

# gets all the users inputs
numbers = []
total = 0
while True:
    user_input = input("Enter a number (press Enter to finish): ")
    
    # Check if the user input is empty (i.e., Enter key pressed)
    if user_input == '':
        break
    
    # Convert the input to a number (if possible)
    try:
        number = float(user_input)
        numbers.append(number)
        total += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate sum and average
count = len(numbers)
if count > 0:
    average = total / count
    print(f"Sum of the numbers: {total}")
    print(f"Average of the numbers: {average:.2f}")
else:
    print("No valid numbers were entered.")
