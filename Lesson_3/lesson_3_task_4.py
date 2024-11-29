# Little lion

from turtle import Turtle

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1500, 1000)
my_turtle.screen.bgcolor("lightblue")


def draw_circle(x, y, radius, color):
    my_turtle.penup()
    my_turtle.goto(x, y - radius)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()


def draw_oval(x, y, width, height, color):
    my_turtle.penup()
    my_turtle.goto(x, y - height)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for a in range(2):
        my_turtle.circle(width, 90)
        my_turtle.circle(height, 90)
    my_turtle.end_fill()


def draw_rect(x, y, width, height, color, tilt_angle):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(tilt_angle)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for b in range(2):
        my_turtle.forward(width)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
    my_turtle.end_fill()


def draw_triangle(x, y, side_length, color, tilt_angle):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(tilt_angle)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for c in range(3):
        my_turtle.forward(side_length)
        my_turtle.left(120)
    my_turtle.end_fill()


def draw_arc(x, y, radius, extent, color, line_thickness, tilt_angle):
    my_turtle.penup()
    my_turtle.goto(x, y - radius)
    my_turtle.setheading(tilt_angle)
    my_turtle.pendown()
    my_turtle.pensize(line_thickness)
    my_turtle.pencolor(color)
    my_turtle.circle(radius, extent)
    my_turtle.end_fill()
    my_turtle.pensize(0)


def draw_lion():
    # tail
    draw_arc(198, -44, 100, 110, "brown", 22, 0)

    # hair 1
    draw_triangle(-214, 250, 77, "orange", 85)

    # hair 2
    draw_triangle(-211, 311, 77, "orange", 55)

    # hair 3
    draw_triangle(-177, 358, 77, "orange", 29)

    # hair 4
    draw_triangle(-133, 380, 77, "orange", 3)

    # hair 5
    draw_triangle(-80, 388, 77, "orange", -30)

    # hair 6
    draw_triangle(-33, 366, 77, "orange", -60)

    # hair 7
    draw_triangle(0, 316, 77, "orange", -90)

    # neck
    draw_rect(-130, 120, 80, 80, "orange", 0)

    # head
    draw_circle(-100, 280, 120, "yellow")

    # right front paw
    draw_rect(-199, -5, 80, 330, "orange", 66)

    # left front paw
    draw_rect(60, 70, 80, 330, "orange", 300)

    # right back paw
    draw_rect(-130, -160, 80, 330, "orange", 150)

    # left back paw
    draw_rect(90, -130, 80, 330, "orange", 210)

    # body
    draw_oval(-200, 380, 180, 280, "yellow")

    # mouth
    draw_arc(-128, 270, 55, 66, "red", 11, 333)

    # right eye 1
    draw_circle(-140, 322, 20, "white")

    # left eye 1
    draw_circle(-60, 324, 20, "white")

    # right eye 2
    draw_circle(-148, 325, 9, "black")

    # left eye 2
    draw_circle(-68, 325, 9, "black")

    # nose 1
    draw_circle(-110, 266, 7, "brown")

    # nose 2
    draw_circle(-87, 266, 7, "brown")

    # breast 1
    draw_circle(-144, 44, 7, "brown")

    # breast 2
    draw_circle(0, 48, 7, "brown")

    # belly
    draw_circle(-60, -133, 7, "brown")


draw_lion()
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()
