from turtle import *

speed(0)
hideturtle()
tracer(0, 0)

level_scale = 0.8


def tree(length, level, angle):
    if level == 0:
        # color("purple")
        # dot(length * 0.5)
        # color("black")
        # backward(length)
        return True
    forward(length)
    left(angle)
    tree(length * level_scale, level - 1, angle)

    right(angle * 2)
    tree(length * level_scale, level - 1, angle)
    left(angle)

    backward(length)


sides = 6

for i in range(sides):
    tree(60, 10, 60)
    left(360 / sides)

# tree(50, 10, 20)

mainloop()
