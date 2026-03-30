import turtle
pen=turtle.Turtle()
pen.pencolor("red")
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.pencolor("blue")
pen.right(45)
pen.forward(75)
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.pencolor("green")

for i in range(4):
    pen.forward(50)
    pen.left(90)

turtle.done()