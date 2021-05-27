#A + B -> C, elementary reaction
#A - carbon monoxide, B - chlorine, C - phosgene

import numpy
from matplotlib import pyplot as plt
from scipy.integrate import odeint

#Define parameters for the system
k = 0.004           #Rate constant

Fa0 = 2 * 10**-5
v0 = 2.83 * 10**-7
Ca0 = Fa0 / v0
Fb0 = Fa0           #Equimolar feed condition
Cb0 = Fb0 / v0

rho = 7             #Density of the catalyst particles
Dp = 35 * 10**-6    #Diameter of catalyst particles
Dc = 500 * 10**-6   #Inner diameter of tube
mu = 1.92 * 10**-5
Ac = 1.96 * 10**-7
G = rho * v0 / Ac
phi = 0.4
P0 = 231 * 10**3
alpha = 3.55 * 10**5 #Describe this later in terms of the other constants

#beta = ( (G * (1 - phi)) / (rho * Dp * phi**3) ) * (150 * (1 - phi) * mu / Dp + 1.75 * G)
#alpha = (2 * beta)/(Ac * rho * (1 - phi) * P0)

#Define ODEs
def odes(x, W):
    X = x[0]
    p = x[1]
    
    Ca = Ca0 * ((1 - X) / (1 - 0.5*X)) * p
    Cb = Ca
    
    dXdW = k * Ca * Cb / Fa0
    dpdW = -(alpha / (2 * p)) * (1 - X)
    
    return [dXdW, dpdW]

#Define initial conditions
x0 = [0, 1]

W = numpy.linspace(0, 3.5*10**-6, 1000)

#Solve the odes. Provide ode definitions, initial conditions and array of values of the independent variable

solution = odeint(odes, x0, W)

X = solution[:, 0]
p = solution[:, 1]

Fa = []
Fc = []

for i in X:
    Fa.append(Fa0 * (1 - i))
    Fc.append(Fa0 * X)

Fb = Fa
    