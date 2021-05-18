import matplotlib.pyplot as plt
import numpy
import math
from scipy import optimize

#variables and constants
R = 8.314 
To = 300

def Kc(T):
    Kco = 3
    H = -104645
    return Kco*math.exp(H/R * (1/To - 1/T))

def z(T):   
    zo = 1.304347826
    E = 62787
    return zo*math.exp(E/R * (1/To - 1/T))


def f(X, T): 
    f = X/((1 - X)**2 - (X**2)/Kc(T)) - z(T)
    return f


#root = optimize.newton(f, 0.2, args =(300, ))

T_values = numpy.linspace(250, 350, 200)
X = []
for T in T_values:
    for x in range(100):
        try:
            root = optimize.newton(f, x / 100, args=(T, ))
            if root < 1 and root > 0:
                break
        except: 
            continue
    
    X.append(root)

plt.plot(T_values, X)
