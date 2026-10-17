from turtle import Turtle, Screen
from random import choice


turtle=Turtle()
screen=Screen()
# screen.bgcolor("aquamarine")

turtle.shape("turtle")
turtle.color('blue')


dash_length=11

def num_of_times(n):
    angle = 360/n
    for _ in range(n):
        turtle.forward(60)
        turtle.right(angle)

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
for i in range(3,dash_length):
    colour = choice(colours)
    turtle.color(colour)
    num_of_times(i)


screen.exitonclick()