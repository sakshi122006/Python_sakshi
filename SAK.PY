import turtle
t=turtle.Turtle()
t.color("red")
for i in range(4):
    t.forward(100)
    t.right(90)

state=t._dict
t.penup()
t.goto(-50,-50)
t.pendown()
t.color("blue")
t.circle(50)
t.dict.update(state)
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()