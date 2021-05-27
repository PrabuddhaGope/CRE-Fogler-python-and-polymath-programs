from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy

#define constants
Kc = 0.32   #atm^-1
k = 54  #mol/kg-cat.h.atm
Pa = 10 #atm
Fa = 50 * 10**3 #mol/h
a = 0.0006  #atm^-1

def odes(x, W):
    #assign each variable a place in the x vector
    p = x[0]
    X = x[1]

    #simplify writing odes
    t = (1-X)/(1+X)

    #define each ode
    dpdW = (-a/2*p) * (1 + X)
    dXdW = (k*Pa/Fa) * (t*p) / (1 + Kc*Pa*t*p)**2

    return [dpdW, dXdW]

#Define initial conditions: when W=0, p = 1 and X = 0
x0 = [1, 0]

W = numpy.linspace(0, 5000, 1000)

solution = odeint(odes, x0, W)

p = solution[:, 0]
X = solution[:, 1]

ra = [] #rate of reaction

for i in range(len(X)):
    t = (1-X[i])/(1+X[i])
    rate = (k*Pa*t*p[i]) / (1 + Kc*Pa*t*p[i])**2
    ra.append(rate)

ra = numpy.array(ra)

pressure_drop = plt.plot(W, p, label='Pressure Drop')
conversion = plt.plot(W, X, label='Conversion')
reaction_rate = plt.plot(W, ra, label='Reaction rate')

plt.plot()
plt.legend()
plt.title("Conversion, pressure drop and rate of reaction in a PBR")
plt.xlabel("Weight of catalyst")
#The following line doesn't work for some reason
#plt.legend(['Pressure drop (p)', 'Conversion (X)', 'Reaction rate (ra)'], loc="upper right")

#Finding the weight of catalyst to achieve 70% conversion
print("The maximum conversion occurs when the weight of catalyst is ", numpy.interp(0.7, X, W))

#Finding the weight of catalyst that results in maximum rate of reaction. Note: It's a PBR
#so reaction rate varies across the length of the reactor. So the W that we'll find will 
#give us the point of the reactor at which rate is highest. If we use a hypthetical CSTR - PBR - where
#the rate of reaction across the whole PBR is the same as the exit conditions, this weight
#will be the optimum total weight of catalyst used.

print("The maximum rate of reaction that can be achieved is " , ra.max(), "at weight of catalyst:", W[numpy.argmax(ra)])