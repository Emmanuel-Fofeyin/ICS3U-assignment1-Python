#!/usr/bin/env python3
# Created by: Emmanuel
# Created on: Oct 2022
# This program calculates the Area of a pentagon
# with user input

import math

def main():
    # this function calculates Area

    # input
    side = int(input("input the border length: "))

    # process
    area = 0.25 * (math.sqrt (5 *(5 + 2 * math.sqrt(5)))) * math.pow(side, 2)
    perimeter = 5 * side

    # output
    print("Area of Pentagon is: {:,.2f}".format(area))
    print("Perimeter of Pentagon is: {:,.2f}".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
