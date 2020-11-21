from turtle import Turtle, Screen


def snowflake(length_side, levels):
    if levels == 0:
        t.forward(length_side)
        return
    length_side = length_side / 3
    snowflake(length_side, levels - 1)
    t.left(60)
    snowflake(length_side, levels - 1)
    t.right(120)
    snowflake(length_side, levels - 1)
    t.left(60)
    snowflake(length_side, levels - 1)


def draw_one_flake(length, level):
    t.pendown()
    for i in range(3):
        snowflake(length, level)
        t.right(120)
    t.penup()


t = Turtle()
screen = Screen()
# screen.bgcolor("#3659d9")
filename = "koch_snowflake.eps"

# defining the speed of the turtle
t.speed(99999)
length = 100.0
level = 2
t.pensize(8)
t.hideturtle()

# draw a snowflake circle
for i in range(6):
    t.pencolor("Black")
    draw_one_flake(length, level)
    t.left(120)
    t.forward(length/3)
    t.right(60)
    t.forward(length/3)

# screen.exitonclick()

# save as svg
cv = screen.getcanvas()
cv.postscript(file=filename)
