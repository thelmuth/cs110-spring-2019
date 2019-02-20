
import math

# x = 0
#
# while x ** 3 < 10000:
#     print(x, x**3)
#     x += 1

def newtons_method_sqrt(x):

    tolerance = 0.00001
    guess = 1.0
    last_guess = 2.0 # Just needs to be at least 0.00001 away from guess

    while abs(guess - last_guess) > tolerance:
        last_guess = guess
        guess = (guess + x / guess) / 2

        print(guess)

    return guess

# number = 2999
#
# estimate = newtons_method_sqrt(number)
#
# print("guess:  ", estimate)
# print("actual: ", math.sqrt(number))

# Want to enter integers as the user until we enter a blank line. Collect
# all of those integers in a list.

# Version 1
# numbers = []
# number_as_string = input("Enter a number: ")
#
# while number_as_string != "":
#     number = int(number_as_string)
#     numbers.append(number)
#     number_as_string = input("Enter a number: ")
#
# print(numbers)

# Version 2
numbers = []

while True:
    number_as_string = input("Enter a number: ")
    if number_as_string == "":
        break

    number = int(number_as_string)
    numbers.append(number)

print(numbers)

# Version 3
# DOESN'T QUITE WORK!!!
# numbers = []
# not_done_yet = True
#
# while not_done_yet:
#     number_as_string = input("Enter a number: ")
#     if number_as_string == "":
#         not_done_yet = False
#
#     number = int(number_as_string)
#     numbers.append(number)
#
# print(numbers)
