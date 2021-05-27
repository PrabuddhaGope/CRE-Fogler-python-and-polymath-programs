import matplotlib.pyplot as plt
import numpy
import math
from scipy import optimize

#constants : All values are in SI units
R = 8.314   #universal gas constant
To = 300    #Temperature at which data is given
H = -104645 #Enthalpy of reaction
E = 62787   #Activation energy

def Kc(T):  #Equilibrium constant
    Kco = 3
    return Kco*math.exp(H/R * (1/To - 1/T))

def z(T):   #Grouping together constants
    zo = 1.304347826    
    return zo*math.exp(E/R * (1/To - 1/T))  #In z, the only variable changing is the rate constant.


def f(X, T):
    f = X/((1 - X)**2 - (X**2)/Kc(T)) - z(T)    #Equation resulting from mole balance, rate law, stoichiometry. Written as f = 0
    return f


T_values = numpy.linspace(250, 350, 200) #Generating 200 T values for the range [250,350]
X = []

for T in T_values:
    for x in range(100): #produces x between 0 and 100 so that we can input values to f between 0 to 1
        try:
            root = optimize.newton(f, x / 100, args=(T, ))
            if root < 1 and root > 0:   #check to see if the root is valid (as conversion can't be greater than 1)
                break
        except:
            continue    #If newton method can't find a root, prevent code from returning a traceback/other error and instead try with a new initial guess

    X.append(root)

plt.plot(T_values, X)   #Simple graph between conversion and temperature
