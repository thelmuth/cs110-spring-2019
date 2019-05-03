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


def main():
    # print(my_in(5, [1, 3, 5, 7, 9]))
    # print(my_in(6, [1, 3, 5, 7, 9]))

    time_binary()

main()
