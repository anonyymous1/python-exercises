# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(num_list, n):
    for i in range(len(num_list)):
        num_list[i] = num_list[i] * n
    return num_list


numbers = [11,2,-3,9]
print(multiply_by(numbers, 2))