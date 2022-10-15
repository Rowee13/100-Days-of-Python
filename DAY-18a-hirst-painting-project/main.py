# import colorgram
#
# colors = colorgram.extract('image.jpeg', 50)  # 360
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

timmy = turtle_module.Turtle()
timmy.shape('turtle')
timmy.penup()
timmy.hideturtle()
turtle_module.colormode(255)

color_list = [
    (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142),
    (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15),
    (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183),
    (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196),
    (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49),
    (180, 188, 210), (84, 65, 30), (16, 77, 106)
]
timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
