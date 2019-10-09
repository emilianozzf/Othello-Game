import turtle as t


t.shape("turtle")  # triangle, arrow, classic circle
# t.hideturtle()
t.delay(1)
t.speed("slowest")  # fastest

t.pensize(5)
t.pencolor("red")
t.fillcolor("yellow")

# t.pd()  # pendown, in the state of drawing, default in the beginning
t.begin_fill()
t.forward(200)  # default is to the right
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

t.pu()

t.goto(-100, -50)
t.pencolor("purple")
t.fillcolor("blue")
t.setheading(45)

t.pd()
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()
# t.pu()

t.exitonclick()

t.done()
