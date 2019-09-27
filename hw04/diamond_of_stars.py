# This program, given a number representing the height of the diamond,
# prints out an appropriately-sized diamond of stars.
import sys
WHITESPACE = " "
ASTERISK = "*"


def main(height):
    if height % 2 != 0:
        width = height
        for row in range(1, width, 2):
            print_a_row(width - row, row)
        for row in range(width, 0, -2):
            print_a_row(width - row, row)
    else:
        width = height - 1
        for row in range(1, width + 1, 2):
            print_a_row(width - row, row)
        for row in range(width, 0, -2):
            print_a_row(width - row, row)


def print_a_row(num_of_whitespace, num_of_asterisk):
    """Given the number of whitespaces and the number of asterisks, prints out
    the expected row consists of whitespaces and asterisks."""
    print(WHITESPACE * (num_of_whitespace // 2) +
          ASTERISK * num_of_asterisk +
          WHITESPACE * (num_of_whitespace // 2))

main(int(sys.argv[1]))
