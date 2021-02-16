''' Task 2: Generate a list of 25 random numbers.
The numbers should be between 100 and 1000.
Remove duplicates from the list.
Find maximum and minimum from the list
Generate a new list with only odd numbers from the above random list '''

import random


def odd_numbers_out(numbers):

    output = []
    for i in range(numbers + 1):
        output.append(random.randint(100, 1000))

    uniques = []
    for j in output:
        if j not in uniques:
            uniques.append(j)

    uniques.sort()
    max = 0
    min = 1000

    for num in uniques:
        if num > max:
            max = num
        if num < min:
            min = num

    odd_numubers = []
    for item in uniques:
        if item % 2 != 0:
            odd_numubers.append(item)
            # print(odd_numubers)

    return odd_numubers

print(odd_numbers_out(25))