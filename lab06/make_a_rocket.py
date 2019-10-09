import sys
SPACE = ' '
ASTERISK = '*'
CAPITAL_X = 'X'
UNDERSCORE = '_'


def main(width, length, optional_argument=None):
    draw_nose_cone(width)
    draw_fuselage(width, length, optional_argument)
    draw_tail_fin(width)


def draw_nose_cone(width):
    for line_width in range(width % 2, width, 2):
        line = (SPACE * ((width - line_width) // 2)) + (ASTERISK * line_width)
        print(line)


def draw_fuselage(width, length, optional_argument=None):
    for num in range(length):
        draw_fuselage_segment(width, optional_argument)


def draw_fuselage_segment(width, optional_argument=None):
    if optional_argument == "striped":
        magic_character = UNDERSCORE
    else:
        magic_character = CAPITAL_X

    for num in range(width // 2):
        print(magic_character * width)

    for num in range(width // 2, width):
        print(CAPITAL_X * width)


def draw_tail_fin(width):
    if (width % 2 != 0) and ((width // 2 % 2) == 0):
        top = width // 2 + 1
    else:
        top = width // 2
    for line_width in range(top, width, 2):
        line = (SPACE * ((width - line_width) // 2)) + (ASTERISK * line_width)
        print(line)
    for num in range(2):
        print(ASTERISK * width)


if len(sys.argv) == 3:
    main(int(sys.argv[1]), int(sys.argv[2]))
else:
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
