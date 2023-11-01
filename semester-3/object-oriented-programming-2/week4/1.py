"""
1. A group of statisticians at a local college has asked you to create a List of functions
that compute the median and mode of a List of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a List of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.
"""
from typing import List
import random
from collections import defaultdict

# found this off stack overflow
population = list(range(1, 101))
weights = [0.3] + [0.7 / 99] * 99
random_integers = random.choices(population, weights=weights, k=100)
sorted_integers = sorted(random_integers)


# gets median for a data List
def median(numbers: List[int]) -> int:
    if not numbers:
        return 0.0

    # divides it by 2 and tries to find the middle number
    target = len(numbers) // 2

    # returns the median
    return numbers[target]


# tries to find to mode of a list
def mode(numbers: List[int]) -> List[int]:
    if not numbers:
        return [0]

    dictionary_of_numbers_and_their_count = defaultdict(int)

    # will automatically add to count and create a new instance of it if it doesnt already exist in the list
    for number in numbers:
        dictionary_of_numbers_and_their_count[number] += 1

    # will see what the maxmim count in the list is
    max_count = max(dictionary_of_numbers_and_their_count.values())

    # tries to find all the numbers that have that count
    mode_numbers = []
    for number, count in dictionary_of_numbers_and_their_count.items():
        # if it has that max count it will add it to the list of numbers with that same count
        if count == max_count:
            mode_numbers.append(number)

    return mode_numbers


# tries to find the mean of these numbers
def mean(numbers: List[int]) -> float:
    if not numbers:
        return 0.0

    # gets a total
    total = sum(numbers)

    # returns the mean
    return total / len(numbers)


median_example = median(sorted_integers)
mode_example = mode(sorted_integers)
mean_example = mean(sorted_integers)

print(f"Sorted List: {sorted_integers}")
print(f"Median: {median_example}")
print(f"Mode: {mode_example}")
print(f"Mean: {mean_example}")
