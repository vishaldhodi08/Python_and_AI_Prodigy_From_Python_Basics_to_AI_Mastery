import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle Square")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(4)
t.speed(3)

# Draw a square
for i in range(4):
    t.forward(150)
    t.right(90)

turtle.done()