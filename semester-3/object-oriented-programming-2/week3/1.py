"""
8. Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file.
"""

write = input("enter text file you want copied: ")
printed = input("enter the text file you was printed on: ")

# gets context to copy
with open(write, "r") as input_file:
    file_content = input_file.read()

# gets content to paste on 
with open(printed, "w") as output_file:
    output_file.write(file_content)



