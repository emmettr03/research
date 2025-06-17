from turtle import *

# Screen setup
setup(800, 600)
bgcolor("skyblue")
speed(0)
hideturtle()

# Utility functions

def draw_rectangle(x, y, width, height, color_name):
    penup()
    goto(x, y)
    color(color_name)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def draw_triangle(x, y, width, height, color_name):
    penup()
    goto(x, y)
    color(color_name)
    begin_fill()
    goto(x + width / 2, y + height)
    goto(x + width, y)
    goto(x, y)
    end_fill()


def draw_horse_logo(x, y, scale=1.0):
    penup()
    goto(x, y)
    pendown()
    color("black")
    pensize(2)

    # Body
    begin_fill()
    circle(20 * scale)
    end_fill()

    # Neck and head
    penup()
    goto(x + 20 * scale, y + 20 * scale)
    pendown()
    goto(x + 35 * scale, y + 50 * scale)
    begin_fill()
    circle(8 * scale)
    end_fill()

    # Front legs (raised)
    penup()
    goto(x + 15 * scale, y + 10 * scale)
    pendown()
    goto(x + 35 * scale, y + 40 * scale)
    penup()
    goto(x + 5 * scale, y + 10 * scale)
    pendown()
    goto(x + 25 * scale, y + 40 * scale)

    # Hind legs
    penup()
    goto(x - 15 * scale, y - 20 * scale)
    pendown()
    goto(x, y)
    goto(x - 5 * scale, y - 20 * scale)
    goto(x, y)

    # Tail
    penup()
    goto(x - 20 * scale, y + 10 * scale)
    pendown()
    goto(x - 40 * scale, y + 20 * scale)


def draw_scene():
    # Grass
    draw_rectangle(-400, -200, 800, 100, "green")

    # School building
    draw_rectangle(-150, -100, 300, 200, "red")

    # Roof
    draw_triangle(-160, 100, 320, 80, "maroon")

    # Door
    draw_rectangle(-30, -100, 60, 100, "brown")

    # Windows
    draw_rectangle(-120, 0, 60, 40, "white")
    draw_rectangle(60, 0, 60, 40, "white")

    # Horsforth School logo (horse)
    draw_horse_logo(0, 50, 1)

    # Text above the school
    penup()
    goto(0, 200)
    color("purple")
    write("Horsforth School", align="center", font=("Arial", 32, "bold"))

    done()


if __name__ == "__main__":
    draw_scene()
