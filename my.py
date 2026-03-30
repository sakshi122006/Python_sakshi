import turtle 
# Create a turtle object
t = turtle.Turtle() 
# Function to move the turtle forward 
def move_forward():
   t.forward(20)
 # Function to move the turtle backward 
def move_backward(): 
  t.backward(20) 
# Function to turn the turtle left 
def turn_left(): 
   t.left(10)
 # Function to turn the turtle right 
def turn_right(): 
  t.right(10) 
# Function to change the turtle's color to red
def set_red_color(): 
   t.color("red")
 # Function to change the turtle's color to green
def set_green_color():
   t.color("green") 
# Function to change the turtle's color to blue 
def set_blue_color(): 
   t.color("blue") 
# Event handling - Keyboard bindings 
turtle.listen() 
# Start listening to keyboard events 
turtle.onkeypress(move_forward, "Up") 
turtle.onkeypress(move_backward, "Down") 
turtle.onkeypress(turn_left, "Left") 
turtle.onkeypress(turn_right, "Right") 
turtle.onkeypress(set_red_color, "r") 
turtle.onkeypress(set_green_color, "g") 
turtle.onkeypress(set_blue_color, "b")
# Keep the window open until it is closed manually
turtle.done()