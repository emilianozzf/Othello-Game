# This program, given an odd number base of a triangle, prints the expeced
# triangle.
TOP = '*'
LEFT_EDGE = '/'
WHITESPACE = ' '
RIGHT_EDGE = '\\'
BASE = '_'


def main():
    # Asks user for a odd number base that is larger than 3
    base = int(input("Enter an odd number base (>= 3): "))
    while base % 2 == 0 or base < 3:
        base = int(input("Enter an odd number base (>= 3): "))

    for i in range(1, base + 1, 2):  # loops through lines
        if i == 1:
            print(((base - i) // 2) * WHITESPACE + TOP +
                  ((base - i) // 2) * WHITESPACE)  # prints the first line
        elif i > 1 and i < base:
            print(((base - i) // 2) * WHITESPACE +
                  LEFT_EDGE + WHITESPACE * (i - 2) + RIGHT_EDGE +
                  ((base - i) // 2) * WHITESPACE)  # prints the second line
        else:
            print(((base - i) // 2) * WHITESPACE +
                  LEFT_EDGE + BASE * (i - 2) + RIGHT_EDGE +
                  ((base - i) // 2) * WHITESPACE)  # prints the last line

main()
