# Beverly Parnell
# P4LAB1 
# October 25, 2026
# This program uses turtle loops to draw a square and a triangle


# Import turtle
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
win.bgcolor("lightpink")
pen.pensize(3)
pen.pencolor("purple")
pen.shape("turtle")

# Code to draw the shapes
for side in range(4):
    pen.forward(150)
    pen.left(90)

# Move to the top of the square
pen.penup()
pen.left(90)
pen.forward(150)
pen.right(90)
pen.pendown()

# While loop that executes 3 times
pen.fillcolor("hotpink")
pen.begin_fill()

sides = 3

while sides > 0:
    pen.forward(150)
    pen.left(120)
    sides = sides - 1

pen.end_fill()

# Draw the door
pen.penup()
pen.goto(55, 0)
pen.setheading(90)
pen.pendown()
pen.forward(80)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.forward(80)

# Add initials
pen.penup()
pen.goto(200, -180)
pen.write("BP", font=("Arial", 16, "bold"))

# Hide turtle
pen.hideturtle()

# Wait for user to close window
win.mainloop()