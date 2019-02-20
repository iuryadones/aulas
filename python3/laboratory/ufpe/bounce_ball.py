import pylab

dt = 1e-7
y = 9
t = 0
v = 0
g = -10
box = [(0, 0),(0, 5)]


V = []
Y = []
V.append(v)
Y.append(y)

flag = False


for _ in range(10000):
    v += g*t
    y += v*t
    t += dt
    if y <= box[0][1]:
        v = -v
        flag = True
    elif y >= box[1][1] and flag:
        v = -v
    V.append(v)
    Y.append(y)


pylab.plot(V,'.')
pylab.xlabel('step')
pylab.ylabel('V')
pylab.show()
 
pylab.plot(Y,'.')
pylab.xlabel('step')
pylab.ylabel('Y')
pylab.show()

turtle.mainloop()
