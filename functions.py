
import math

def main():
    # for r in range(10):
    #     print("The area of a circle with radius", r, "is", area_of_circle(r))

    longer_college = longer("Hamilton College",
                            "Colgate University")
    print(longer_college)
    print(longer("elephant", "zebra"))


def area_of_circle(radius):
    """Calculates the area of a circle"""
    return math.pi * (radius ** 2)

def longer(string1, string2):
    """Returns the longer of string1 and string2"""
    length1 = len(string1)
    length2 = len(string2)
    if length1 > length2:
        return string1
    else:
        return string2


main()
