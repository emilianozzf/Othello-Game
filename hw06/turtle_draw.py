# This program draws a star and a circle

# Imports turtle and math libraries
import turtle as t
import math

# Sets some useful magical numbers as global constants
# The x coordinate of the circle's center is 0
CENTER_X_COORD = 0
# The y coordinate of the circle's center is 0
CENTER_Y_COORD = 0
# The radius of the circle is 263 pixels
RADIUS = 263
# The degrees of a whole circle is 360
DEGS_IN_CIRC = 360
# The incrementing degrees for drawing the circle is 1
INCR_DEGS = 1
# The beginning degrees for drawing the star is 18
BEGIN_DEGS = 18
# The beginning heading degrees for drawing the star is 180
BEGIN_HEADING_DEGS = 180
# The star's segment is 500 pixels long
STAR_SEG = 500
# The tip turning degrees for drawing the star is 144
TIP_TURN_DEGS = 144


def main():
    # Draws the circle
    draw_circle(CENTER_X_COORD, CENTER_Y_COORD, RADIUS)
    # Draws the star
    draw_star(CENTER_X_COORD, CENTER_Y_COORD, RADIUS, STAR_SEG)
    # Exits on click
    t.exitonclick()


def draw_circle(center_x_coord, center_y_coord, radius):
    """
    Given the circle's center coordinates and radius, draws the circle
    Number Number Number -> None
    """
    # The outline of the circle is blue
    t.pencolor("blue")
    # The fill of the circle is cyan
    t.fillcolor("cyan")
    # Takes up the pen for moving
    t.pu()
    # Takes the pen to the starting point
    t.goto(center_x_coord + radius, center_y_coord)
    # Puts down the pen for drawing
    t.pd()
    # Begins filling
    t.begin_fill()
    # Draws the circle
    for angle in range(0, DEGS_IN_CIRC + 1, INCR_DEGS):
        t.goto(center_x_coord + radius*math.cos(math.radians(angle)),
               center_y_coord + radius*math.sin(math.radians(angle)))
    # Ends filling
    t.end_fill()
    # Takes up the pen for moving
    t.pu()


def draw_star(center_x_coord, center_y_coord, radius, star_seg):
    """
    Given the circle's center coordinates, radius and the star's segment's
    length, draws the star
    Number Number Number Number -> None
    """
    # The outline of the star is red
    t.pencolor("red")
    # The fill of the star is yellow
    t.fillcolor("yellow")
    # Takes up the pen for moving
    t.pu()
    # Takes the pen to the starting point
    t.goto(center_x_coord + radius*math.cos(math.radians(BEGIN_DEGS)),
           center_y_coord + radius*math.sin(math.radians(BEGIN_DEGS)))
    # Sets the pen's beginning heading direction
    t.setheading(BEGIN_HEADING_DEGS)
    # Puts down the pen for drawing
    t.pd()
    # Begins filling
    t.begin_fill()
    # Draws the star
    t.forward(star_seg)
    t.left(TIP_TURN_DEGS)
    t.forward(star_seg)
    t.left(TIP_TURN_DEGS)
    t.forward(star_seg)
    t.left(TIP_TURN_DEGS)
    t.forward(star_seg)
    t.left(TIP_TURN_DEGS)
    t.forward(star_seg)
    # Ends filling
    t.end_fill()
    # Takes up the pen for moving
    t.pu()


main()
