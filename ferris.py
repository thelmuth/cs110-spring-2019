"""This is the ferris wheel program."""

import math

FEET_PER_MILE = 5280

def main():
    height = int(input("Enter the height of the ferris wheel in feet: "))
    dist_miles = float(input("Enter the distance the ferris wheel has traveled in miles: "))

    dist_feet = FEET_PER_MILE * dist_miles
    circ = math.pi * height

    rotations = int(dist_feet / circ)
    feet_past_last_rotation = round(dist_feet % circ)

    print("The ferris wheel rotated", rotations, "times.")
    print("The outside traveled", feet_past_last_rotation, "feet past the last rotation.")



main()
