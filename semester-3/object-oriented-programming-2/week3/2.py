"""
10. Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found.
"""
# gets the inputs
first_file = input("Enter the first file: ")
second_file = input("Enter the second file: ")

# opens and reads first input
with open(first_file, "r") as first:
    first_file_contents = first.read()

#opens and reads the second input
with open(second_file, "r") as second:
    second_file_contents = second.read()

# if they are both the same then it finishes right there
if first_file_contents == second_file_contents:
    print("Yes")

#if theyre not the same then it does this 
else:
    print("No") # tells user its not the same
    output_string = "" # initalizes a string we will add to
    length = min(len(first_file_contents), len(second_file_contents)) # whichever string is shorter itll bring that number back for the length
    for i in range(length):# loops through that lengths
        if first_file_contents[i] == second_file_contents[i]: # if they both share index i itll move on to the next number until it finds the error
            output_string += first_file_contents[i] #adds the letter that is correct to the string
        else:
            break

    print(output_string) # return to string that shows the parts that are the same