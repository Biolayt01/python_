import random
import turtle as t
import random


turtle=t.Turtle()
screen=t.Screen()
t.colormode(255)
screen.colormode(255)

screen.bgcolor("aquamarine")

dash_length=400
def ran_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def random_walk(n):
    for i in range(1,n,10):
        radius = 100
        turtle.color(ran_colour())
        turtle.width(2)
        turtle.circle(radius)
        turtle.seth(i)


if __name__ == '__main__':
    random_walk(dash_length)

    screen.exitonclick()