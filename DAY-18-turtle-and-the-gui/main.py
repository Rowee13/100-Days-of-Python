import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.shape('turtle')
timmy.color('green4')
timmy.speed('fastest')
# timmy.pensize(10)


# colours = [
#     'aquamarine', 'blue', 'red', 'DarkGoldenrod1', 'chartreuse', 'gold1', 'lawngreen', 'khaki1',
#     'orange', 'magenta', 'yellow', 'purple', 'RoyalBlue1', 'SkyBlue1', 'tomato', 'SandyBrown',
# ]

# ======draw dash lin=====
# for _ in range(30):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# ======changing shape======
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

# =======Random Walk=======
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     pick_color = (r, g, b)
#     return pick_color
#
#
# direction = [0, 90, 180, 270]
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))
#     timmy.pensize(10)


# =======Spirograph========
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pick_color = (r, g, b)
    return pick_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
