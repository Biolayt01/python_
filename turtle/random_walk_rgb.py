import random
import turtle as t
import random


turtle=t.Turtle()
screen=t.Screen()
t.colormode(255)
screen.colormode(255)

screen.bgcolor("aquamarine")

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
def ran_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

for i in range(dash_length):
    turtle.color(ran_colour())
    turtle.pensize(width=5)
    random_walk(i)


screen.exitonclick()