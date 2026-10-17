import random
from turtle import Turtle, Screen
import random


turtle=Turtle()
screen=Screen()
screen.bgcolor("aquamarine")

turtle.shape("turtle")
turtle.color('blue')


dash_length=50

def random_walk(n):
    for i in range(n):

        movement = ['forward','backward','left','right']

        move = random.choice(movement)

        if move == 'forward':
            turtle.forward(10)
        elif move == 'backward':
            turtle.backward(10)
        elif move == 'left':
            turtle.left(90)
        else:
            turtle.right(90)


# random_walk(dash_length)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'violet','indigo','coral','magenta']
for i in range(dash_length):
    turtle.color(random.choice(colours))
for i in range(dash_length):
    colour = random.choice(colours)
    turtle.color(colour)
    turtle.pensize(width=5)
    random_walk(i)


screen.exitonclick()