
# Store the square of the numbers between given numbers in an array

def square_numbers(num1, num2):

    square = [num*num for num in range(num1, num2 + 1)]

    return square


print(square_numbers(5, 15))