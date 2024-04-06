import turtle
import random

# Set up the turtle screen
turtle.setup(width=800, height=800)
turtle.speed('fastest')
turtle.bgcolor('black')


# Define a function to draw the shapes
def draw_shapes(word):
    # Set the parameters based on the first and second letters of the word
    param1 = ord(word[0]) % 360
    param2 = (ord(word[1]) - 64) * 5

    # Loop to draw the shapes
    for i in range(1000):
        turtle.color(random.random(), random.random(), random.random())
        turtle.forward(i * param1)
        turtle.right(param2)

    turtle.done()


# Get input from the user
word = input("Enter a word to generate a spiral and repeating geometric shapes: ")

# Call the draw_shapes function
draw_shapes(word)
