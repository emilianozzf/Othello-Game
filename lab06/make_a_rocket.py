# The program takes the width of the rocket, the length of the rocket's
# fuselage in square segments, and one optional argument the word "striped",
# and prints out an expeted rocket consisting of a nose cone, a fuselage, and
# a tail fin structure.

import sys

# Stores all the drawing characters as constants
# This is a whitespace
SPACE = ' '
# The nose cone and tail structure are composed of * characters.
ASTERISK = '*'
# The fuselage is made up of X characters by default.
CAPITAL_X = 'X'
# The first half of the fuselage is made up of _ characters with the
# striped argument
UNDERSCORE = '_'


def main(width, length, optional_argument=None):
    # Draws the nose cone of the rocket
    draw_nose_cone(width)
    # Draws the fuselage of the rocket
    draw_fuselage(width, length, optional_argument)
    # Draws the tail fin of the rocket
    draw_tail_fin(width)


def draw_nose_cone(width):
    """Draws the nose cone of the rocket
    Integer -> None"""
    # Draws the nose cone line by line
    for line_width in range(width % 2, width, 2):
        line = (SPACE * ((width - line_width) // 2)) + (ASTERISK * line_width)
        print(line)


def draw_fuselage(width, length, optional_argument=None):
    """Draws the fuselage of the rocket
    Integer Integer String -> None"""
    # Draws the fuselage line by line
    for num in range(length):
        draw_fuselage_segment(width, optional_argument)


def draw_fuselage_segment(width, optional_argument=None):
    """Draws the fuselage segment
    Integer String -> None"""
    # Checks if the striped argument is passes in
    if optional_argument == "striped":
        # Uses the _ characters to draw the first half of the fuselage segment
        magic_character = UNDERSCORE
    else:
        # Uses the X characters to draw the first half of the fuselage segment
        magic_character = CAPITAL_X
    # Draws the first half of the fuselage segment line by line
    for num in range(width // 2):
        print(magic_character * width)
    # Draws the second half of the fuselage segment line by line
    for num in range(width // 2, width):
        print(CAPITAL_X * width)


def draw_tail_fin(width):
    """Draws the tail fin of the rocket
    Integer -> None"""
    # Modifies the top line width of the tail fin
    if (width % 2 != 0) and ((width // 2 % 2) == 0):
        top = width // 2 + 1
    else:
        top = width // 2
    # Draws the tail fin line by line
    for line_width in range(top, width, 2):
        line = (SPACE * ((width - line_width) // 2)) + (ASTERISK * line_width)
        print(line)
    # Draws the rest 2 lines of the tail fin
    for num in range(2):
        print(ASTERISK * width)


# Checks if the length of sys.argv array is 3
if len(sys.argv) == 3:
    # Passes in the second and the third command line arguments
    main(int(sys.argv[1]), int(sys.argv[2]))
else:
    # Passes in the second, the third , and the fourth command line arguments
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
