import turtle
t=turtle.Turtle()
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(0)
def turn_left():
    t.left(10)
def turn_right():
    t.right(10)

screen=turtle.Screen()
screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress (turn_left, "Left")
screen.onkeypress (turn_right, "Right")
turtle.mainloop()