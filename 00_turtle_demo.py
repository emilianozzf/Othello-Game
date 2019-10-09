import turtle as turtle
import random as rnd
import math
import tkinter

DEGS_IN_CIRC = 360
INCR_DEGS = 12
BOTTOM_EDGE = 200
OUTER_EDGE = 50
BOTTOM_TIP_ANGLE = 60
TOP_TIP_ANGLE = 130
TOP_EDGE = 230
BG_COLOR = (0.8, 0.95, 0.9)

screen = turtle.getscreen()
screen.bgcolor(BG_COLOR)
width = screen.window_width()
height = screen.window_height()
turtle.shape("turtle")
turtle.delay(0)
turtle.speed("fastest")
# turtle.exitonclick()

while True:
    w = rnd.randint(0, width-1)
    h = rnd.randint(0, height-1)
    turtle.pu()
    turtle.goto(w - width/2, h - height/2)
    turtle.pd()

    stroke_color = 'green'
    for angle in range(0, DEGS_IN_CIRC, INCR_DEGS):
        turtle.setheading(angle)
        fill_color = (math.cos(math.radians(angle)) + 1)/2
        turtle.fillcolor(fill_color, fill_color, fill_color)
        turtle.begin_fill()
        turtle.pencolor(stroke_color)
        turtle.forward(BOTTOM_EDGE)
        turtle.left(BOTTOM_TIP_ANGLE)
        turtle.forward(OUTER_EDGE)
        turtle.left(TOP_TIP_ANGLE)
        turtle.forward(TOP_EDGE)
        turtle.end_fill()
