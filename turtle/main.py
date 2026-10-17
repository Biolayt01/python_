from turtle import Turtle, Screen


turtle=Turtle()
screen=Screen()
screen.bgcolor("aquamarine")

turtle.shape("turtle")
turtle.color('maroon')


dash_length=20

for _ in range(dash_length):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen.exitonclick()