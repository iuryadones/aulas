#!/usr/bin/env python3
import turtle
import random


def main():
    joe = turtle.Turtle(shape='turtle')
    joe.color('black', 'green')

    proba = 0.5

    for _ in range(100):
        joe.forward(distance=10)

        if random.random() < proba:
            joe.right(angle=180)

    turtle.mainloop()


if __name__ == "__main__":
    main()
