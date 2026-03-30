import turtle
t=turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200,0)
t.pendown()


def draw_square():
    for i in range(4): 
        t.forward(100)
        t.right(90)
    for i in range(20):
        t.penup()
        t.forward(20)

t.pendown()

draw_square()
turtle.done()