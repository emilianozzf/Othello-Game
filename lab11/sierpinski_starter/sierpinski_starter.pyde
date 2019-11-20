# ControlP5 is a 3rd party library that gives us
# interface controls. We need it for the slider.
add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider

# Here we import the Point class definition from
# the other tab of this sketch. That file is
# and ordinary .py file stored in the same
# sketch directory.
from point import Point

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


def setup():
    """This code is executed only once, at the beginning
    of your sketch. Conceptually, the setup function has
    a similar role to a class's constructor"""
    size(430, 400)
    noStroke()
    setupSlider()


def draw():
    """The draw method is executed repeatedly, coinciding
    with screen refreshes. Anything that needs to be
    redrawn, recalculated, animated, or to respond to
    user interaction will need to be carried out within the
    draw loop."""
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    """This is a recursive function that draws the Sierpinski triangle"""
    fill(0)
    # Base case
    if recursionDepth == 0:
        return
    else:
        # Get midpoints for 3 sides of the triangle
        leftMid = bottomLeft.midPoint(top)
        rightMid = bottomRight.midPoint(top)
        bottomMid = bottomLeft.midPoint(bottomRight)
        # Draw a Sierpinski triangle
        triangle(leftMid.getX(), leftMid.getY(),
                 rightMid.getX(), rightMid.getY(),
                 bottomMid.getX(), bottomMid.getY())
        # Update the recursion depth by -1
        recursionDepth -= 1

        # Recursively draw the next depth Sierpinski triangles
        sierpinksi(bottomLeft, bottomMid, leftMid, recursionDepth)
        sierpinksi(bottomMid, bottomRight, rightMid, recursionDepth)
        sierpinksi(leftMid, rightMid, top, recursionDepth)


def setupSlider():
    """Set up the slider and sets a listener callback
    function to respond to the user sliding the slider."""
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    global depth
    depth = event.value()
