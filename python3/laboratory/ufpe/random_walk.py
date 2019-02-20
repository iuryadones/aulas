import turtle
import random as rd
import pylab as plb


drunk = turtle.Turtle(shape='circle')

step = 10
p_step = 0.7
p_angle = 0.5

X_drunk = []

for _ in range(100):
    print(drunk.pos())

    X_drunk.append(drunk.pos()[0])

    if rd.random() < p_angle:
        drunk.left(90)
    else:
        drunk.left(-90)

    if rd.random() < p_step:
        drunk.forward(step)
    else:
        drunk.backward(step)

plb.plot(X_drunk, '-')
plb.title('Random Walk - Drunk')
plb.ylabel('X')
plb.xlabel('Time(step)')
plb.show()
plb.close()

plb.hist(X_drunk, 10)
plb.show()
plb.close()

turtle.mainloop()

