#!/usr/bin/env python3
import math as m
import pylab as plt


N = 2 ** 6

f = [
    1 * m.cos(2 * m.pi * 5 * (t / N)) +
    1 * m.cos(2 * m.pi * 25 * (t / N)) +
    1 * m.cos(2 * m.pi * 10 * (t / N))
    for t in range(N)
]

print(f, end='\n\n')

F = lambda k: sum([
        f[n] * m.e ** ((-2j * m.pi * n * k) / N)
        for n in range(N)
    ])

F = [F(k) for k in range(N)]

R = [r.real for r in F]

print(R, end='\n\n')

f = lambda n: (1 / N) * sum([
        F[k] * m.e ** ((2j * m.pi * n * k) / N)
        for k in range(N)
    ])

f = [f(n).real for n in range(N)]

print(f, end='\n\n')

plt.figure()
plt.subplot(311)
plt.plot(f)
plt.title('Sinal')
plt.xlabel(r'$t$')
plt.ylabel(r'$Amplitude$')

plt.subplot(312)
markerline, stemlines, baseline = plt.stem(R[:int(len(R) / 2)+1], 'b-.')
plt.setp(baseline, color='r', linewidth=2)
plt.title('Transformada de Fourier (t)')
plt.xlabel(r'$f$')
plt.ylabel(r'$Amplitude$')

plt.subplot(313)
plt.plot(f)
plt.title('Transformada inversa de Fourier (f)')
plt.xlabel(r'$t$')
plt.ylabel(r'$Amplitude$')
plt.tight_layout()
plt.show()
plt.close()

