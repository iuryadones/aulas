#!/usr/bin/env python3
import turtle

def main():
    joe = turtle.Turtle(shape='turtle')
    joe.color('black', 'green')

    joe.forward(distance=100)
    joe.right(angle=90)

    joe.forward(distance=100)
    joe.right(angle=90)

    joe.forward(distance=100)
    joe.right(angle=90)

    joe.forward(distance=100)
    joe.right(angle=90)

    turtle.mainloop()

if __name__ == "__main__":
    main()
