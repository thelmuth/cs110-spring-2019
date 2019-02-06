
# for i in range(10):
#     print(i)

# for x in range(5, 10):
#     print("x is now", x)

# for x in range(5, 20, 3):
#     print(x)

# Loop over the characters in a string
# for char in "hello class":
#     print("the character is:", char)

# Sum the integers between 0 and 9 inclusive
# sum = 0
# for x in range(10):
#     sum = sum + x
#     print(sum)
#
# # Product of integers between 1 and 9
# product = 1
# for h in range(1, 10):
#     product = product * h
#     print(product)

# def main():
#     divisor = float(input("Enter a number to divide 1 by: "))
#     if divisor == 0.0:
#         print("Sorry, you can't divide by 0")
#     else:
#         print("1 divided by", divisor, "is", 1 / divisor)
#         print("yay!")
#
#     print("done here!")
#
# main()

# string = input("Enter a string: ")
# vowels_seen = ""
# counter = 0
# for c in string:
#     if c in 'aeiou':
#         counter = counter + 1
#         if c not in vowels_seen:
#             print(c)
#         vowels_seen = vowels_seen + c
#
# print("The number of vowels was", counter)
# print("All of the vowels are:", vowels_seen)

my_string = "Loik befire yiu loip!"
new_string = ""
for char in my_string:
    if char == "i":
        new_string = new_string + "o"
    else:
        new_string = new_string + char
print(new_string)
