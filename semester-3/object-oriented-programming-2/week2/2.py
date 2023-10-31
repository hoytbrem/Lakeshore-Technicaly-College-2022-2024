# page 100 problem 5

# function to get positive valid integer
def input_valid_positive_integer(input_string):
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
def input_valid_positive_float(input_string):
    user_input = -1
    while True:
        try:
            user_input = float(input(input_string))
            if user_input > 0:
                return user_input
            print("Enter a positive number")
        except ValueError:
            print("Invalid entry, try again")

# function to get the population growth
def predict_population_growth(initial_population, growth_rate, growth_period, hours):
    final_population = initial_population * (growth_rate ** (hours / growth_period))
    return final_population
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~












# Get the user inputs
initial_population = input_valid_positive_integer("Enter the initial number of organisms: ")
growth_rate = input_valid_positive_float("Enter the growth rate: ")
growth_period = input_valid_positive_integer("Enter the number of hours it takes to achieve this rate: ")
hours = input_valid_positive_integer("Enter the number of hours during which the population grows: ")

# Predict the population growth
final_output = predict_population_growth(initial_population, growth_rate, growth_period, hours)

# Display the prediction
print(f"Predicted population after {hours} hours: {final_output:.2f}")
