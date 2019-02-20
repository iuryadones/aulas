import turtle
import random as rd
import pylab as plb
import time


def go(obj,x=0,y=0):
    obj.penup()
    obj.goto(x, y)
    obj.pendown()

def square(obj,size):
    for _ in range(4):
        obj.forward(size)
        obj.left(90)

joe = turtle.Turtle()

go(joe, x=0, y=0)
square(joe, 100)

go(joe, x=100, y=100)
square(joe, 100)

go(joe, x=-100, y=100)
square(joe, 100)

go(joe, x=100, y=-100)
square(joe, 100)

turtle.mainloop()

