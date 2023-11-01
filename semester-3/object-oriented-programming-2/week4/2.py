"""
2. Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.
"""


def read_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


file_name = input("Input the file name: ")

lines = read_file(file_name)

num_lines = len(lines)

while True:
    print(f"\nNumber of lines in the file: {num_lines}")
    line_number = int(input("Enter a line number (1 to N, or 0 to quit): "))

    if line_number == 0:
        break
    elif 1 <= line_number <= num_lines:
        print(f"Line {line_number}: {lines[line_number - 1]}")
    else:
        print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")
