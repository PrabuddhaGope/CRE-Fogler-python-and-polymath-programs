import scipy, numpy, math, sympy
import matplotlib.pyplot as plt

K_c = 0.32
k = 0.054
P_a = 10
F_a = 50 * 10**3

x = sympy.Symbol('x')
f =  (1 + K_c * P_a * (1-x)/(1+x) )**2  / (k * P_a * (1 - x)/(1 + x))


X_values = numpy.linspace(0, 1, 10)
W_values = []
ra_values = []

for i in range(0, 10):
    W = sympy.integrals.integrals.integrate(f, (x, 0,  i /10))
    ra = (k*P_a*(1-i)/(1+i))/(1 + K_c*P_a*(1-i)/(1+i))**2
    W_values.append(W)
    ra_values.append(ra)

plt.plot(W_values, ra_values)

