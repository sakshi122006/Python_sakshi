import turtle
import math

#Setup screen and turtle
screen = turtle.Screen()
screen.bgcolor("lightpink")
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(5)

#Rectangle function
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

#Triangle function
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

#Parallelogram function
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(30)  # Reset direction
    t.end_fill()


t.penup()
t.goto(-150, -120)
t.setheading(0)
t.pendown()
drawRectangle(t, 100, 110, "blue")


t.penup()
t.goto(-120, -120)
t.setheading(0)
t.pendown()
drawRectangle(t, 40, 60, "lightgreen")

#Roof (front triangle)
t.penup()
t.goto(-150, -10)
t.setheading(0)
t.pendown()
drawTriangle(t, 100, "magenta")

#Side wall
t.penup()
t.goto(-50, -120)
t.setheading(0)
t.pendown()
drawParallelogram(t, 60, 110, "yellow")

#Side window
t.penup()
t.goto(-30, -60)
t.setheading(0)
t.pendown()
drawParallelogram(t, 20, 30, "brown")

#Side roof
t.penup()
t.goto(-50, -10)
t.setheading(0)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)  # Reset angle
t.end_fill()

turtle.done()