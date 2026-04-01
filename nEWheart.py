import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Heart ❤️")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("red")

def draw_heart(size):
    pen.clear()
    pen.penup()
    pen.goto(0, -size / 2)
    pen.pendown()
    pen.begin_fill()

    pen.left(140)
    pen.forward(size)
    pen.circle(-size / 2, 200)
    pen.left(120)
    pen.circle(-size / 2, 200)
    pen.forward(size)

    pen.end_fill()
    pen.setheading(0)

# Animation loop
while True:
    draw_heart(100)
    time.sleep(0.3)
    draw_heart(120)
    time.sleep(0.3)