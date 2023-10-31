# Page 99 probelm 4

# Define a function to get a valid positive integer input
def input_valid_positive_integer(item):
    user_input = -1
    while True:
        try:
            user_input = int(input(f"Enter {item}: "))
            if user_input > 0:
                return user_input
            print("Enter a positive number")
        except ValueError:
            print("Invalid entry, try again")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Get valid input for height
height = input_valid_positive_integer("Height")

# Get valid input for the number of bounces
bounces = input_valid_positive_integer("Bounces")

# creates the output
finalAmount = 0
while(bounces != 0):
    bounces -= 1

    # going down
    finalAmount += height
    print(f"Down {finalAmount}")

    # going up 
    height = height * 0.60
    finalAmount += height
    print(f"Up {finalAmount}")

# outputs the final amount
print(f"Your final amount: {finalAmount}")

