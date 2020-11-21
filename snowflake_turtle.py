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

def draw_snowflake_circle(length, level):
    t.penup()
    t.forward(length) # starting to draw snowflake right from center

    for i in range(6):
        t.pencolor("Black")
        draw_one_flake(length, level)
        t.left(120)
        t.forward(length/3)
        t.right(60)
        t.forward(length/3)

def draw_snowflake_pattern(length, level):
    t.penup()
    t.setposition(0,length - int(length/(3*level)))

    for j in range(int((height + length/2)/length )):
        for i in range(int((width + length/2)/length )):
            draw_one_flake(length, level)
            t.penup()
            x, y = t.position()
            t.setposition(x + length, y)

        x, y = t.position()
        t.penup()
        t.setposition(0, y + length + int(length/(3*level)))

t = Turtle()
screen = Screen()
width, height = (1050, 1480)
screen.setup(width, height)
screen.setworldcoordinates(0, 0, width, height)
# screen.bgcolor("#3659d9")
filename = f"koch_snowflake_{width}_{height}.eps"

# defining the speed of the turtle
t.speed(99999)
length = 150.0
level = 2
t.pensize(3)
# t.hideturtle()\\
#
t.hideturtle()
draw_snowflake_pattern(length, level)
# save as svg
cv = screen.getcanvas()
cv.postscript(file=filename)

screen.exitonclick()

