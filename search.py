import time

def my_in(element, things):
    """This should do the same thing as 'in', using a list things."""

    for x in things:
        if x == element:
            return True

    return False


def binary_in(element, things):
    """Uses binary search over sorted list of things."""

    left = 0
    right = len(things) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if element == things[midpoint]:
            return True
        elif element < things[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return False


def time_binary():

    numbers = list(range(10000000))

    target1 = 7832594
    target2 = 88888888888

    start_in = time.perf_counter()

    print("Starting in")
    print(target1 in numbers)
    print(target2 in numbers)

    end_in = time.perf_counter()

    print("The in search took:", end_in - start_in, "seconds")
    print()

    start_binary = time.perf_counter()

    print(binary_in(target1,numbers))
    print(binary_in(target2,numbers))

    end_binary = time.perf_counter()

    print("The binary search took:", end_binary - start_binary, "seconds")
    print()


def find_first_long_word(words):
    """Given a list of words, finds the first word with > 6 letters."""
    for word in words:
        if len(word) > 6:
            return word
    return None


def find_first_that_passes_test(things, test_function):
    """Generalized to find first element that makes test_function True."""

    for element in things:
        if test_function(element):
            return element
    return None

def my_filter(things, test_function):
    """Generalized to find a list of all elements that make test_function True."""
    collection = []
    for element in things:
        if test_function(element):
            collection.append(element)
    return collection

def starts_with_vowel(word):
    return word[0] in "aeiou"

def even(num):
    return num % 2 == 0

def main():
    # print(my_in(5, [1, 3, 5, 7, 9]))
    # print(my_in(6, [1, 3, 5, 7, 9]))

    # time_binary()

    sentence = ["this", "word", "is", "extremely", "long"]

    # print(find_first_long_word(sentence))

    # print(find_first_that_passes_test(sentence, starts_with_vowel))
    # print(find_first_that_passes_test(range(20), even))
    #
    # print(my_filter(sentence, starts_with_vowel))
    # print(my_filter(range(20), even))
    #
    # print(list(filter(starts_with_vowel, sentence)))
    # print(list(filter(even, range(20))))

    numbers = list(range(100))

    evens = [x for x in numbers if even(x)]
    evens = [x for x in numbers if x % 2 == 0]

    vowels = [word for word in sentence if word[0] in "aeiou"]

    #print(vowels)

    # Squares of numbers between 1 and 10
    # print([num ** 2 for num in range(1, 11)])

    print([num ** 2 for num in range(1, 11) if num % 2 == 0])

    # How would you get a list of uppercase words whose length is < 5?
    print([word.upper() for word in sentence if len(word) < 5])

    print([char for char in "ahfoiwhncapicwaip" if char in "aeiou"])








main()
