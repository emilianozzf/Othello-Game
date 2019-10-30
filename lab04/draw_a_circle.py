# This programs, given a radius of a circle, prints the expected circle.
import sys
import math
CIRCLE_CHAR = "o"
WHITESPACE = " "


def main(radius):
    center = (radius, radius - 1)  # determines the center of the circle

    for i in range(2 * radius):  # loops through lines
        row = ""  # set row string to empty
        for j in range(2 * radius):  # loops through columns
            if math.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2) < radius:
                row += CIRCLE_CHAR  # concatenates "o" with the row string
                # if the position to the center is less than radius
            else:
                row += WHITESPACE  # concatenates whitespace otherwise
        print(row)  # prints the row string


main(int(sys.argv[1]))
