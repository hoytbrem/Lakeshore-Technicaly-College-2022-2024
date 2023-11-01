"""
7. Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.
"""


def get_unique_words(filename):
    # uses set because it doesnt allow duplicates
    unique_words = set()

    try:
        # opens a file
        with open(filename, "r") as file:
            # goes through each line
            for line in file:
                # splits where there are spaces
                words = line.split()

                # for each of those words in the line it does this stuff
                for word in words:
                    # gets rid of all special characters and sends it all to lowercase
                    word = word.strip('.,!?";:').lower()
                    # adds the words to the set and if its a duplicate it deletes it
                    unique_words.add(word)
    # if the file input failed it'll shoot an error
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    # it will sort the set and return it
    return sorted(unique_words)


filename = input("Enter the filename: ")
unique_words = get_unique_words(filename)

# if unique_words isnt null itll do this
if unique_words:
    print("Unique words in alphabetical order:")

    # prints everysingle word
    for word in unique_words:
        print(word)
