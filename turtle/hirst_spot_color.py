# import colorgram
#
# number_of_colors = 10
# colours  = colorgram.extract('image.jpg', number_of_colors)
#
# colour = []
# for i in range(number_of_colors):
#     rgb = colours[i].rgb
#     red=rgb[0]
#     green=rgb[1]
#     blue=rgb[2]
#     color = (red,green,blue)
#     colour.append(color)
# print(colour)
import turtle as t

turtle = t.Turtle()
scr = t.Screen()

colour_list=[(235, 234, 232), (235, 232, 234), (184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48)]
def number_of_dotting():
    for _ in range(1,10):
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.dot(20)

for _ in range(1):
    number_of_dotting()
    print(turtle.position())
    turtle.setposition(0.00,)
scr.exitonclick()
