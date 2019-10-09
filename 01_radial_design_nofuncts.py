import turtle as t
import random as rnd
import math

DEGS_IN_CIRC = 360
INCR_DEGS = 12
BOTTOM_EDGE = 200
OUTER_EDGE = 50
BOTTOM_TIP_ANGLE = 60
TOP_TIP_ANGLE = 130
TOP_EDGE = 230
BG_COLOR = (0.8, 0.95, 0.9)

screen = t.getscreen()
screen.bgcolor(BG_COLOR)
width = screen.window_width()
height = screen.window_height()
t.shape("turtle")
t.delay(0)
t.speed("fastest")
# t.exitonclick()

while True:
    w = rnd.randint(0, width-1)
    h = rnd.randint(0, height-1)
    t.pu()
    t.goto(w - width/2, h - height/2)
    t.pd()

    stroke_color = 'green'
    for angle in range(0, DEGS_IN_CIRC, INCR_DEGS):
        t.setheading(angle)
        fill_color = (math.cos(math.radians(angle)) + 1)/2
        t.fillcolor(fill_color, fill_color, fill_color)
        t.begin_fill()
        t.pencolor(stroke_color)
        t.forward(BOTTOM_EDGE)
        t.left(BOTTOM_TIP_ANGLE)
        t.forward(OUTER_EDGE)
        t.left(TOP_TIP_ANGLE)
        t.forward(TOP_EDGE)
        t.end_fill()
