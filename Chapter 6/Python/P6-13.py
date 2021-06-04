#The flowrate entering the reactor as well as the product flowrate have all been expressed in terms of the conversion and the 
#fraction,f of unreacted effluent that has been recycled
import numpy 
from scipy import optimize
from matplotlib import pyplot as plt

v0 = 12 # Fresh feed
Ca0 = 100 #Density as well as weight concentration of A(and B)
V = 60 #Reactor volume
k = 0.4 #rate constant
Kc = 4 #Equilibrium constant

# Relation between X and f (obtained using the CSTR algorithm)
def g(X, f):
    return v0 * X / (V * (1 - f * (1 - X))) - k * (1 - X - X / Kc)

# Objective function for evaluation of profits
def h(X, f):
    return (v0 / (1 - f * (1 - X))) * (200 * X - 50)

# For values of f between 0 and 1, generate corresponding values of X
f_values = numpy.linspace(0, 1, 100)
X_values = []

for f in f_values:
    X = optimize.newton(g, 0.5, args=(f, ))
    X_values.append(X)
    
# For each set of values of f and X, evaluate the objective function   
profit_values = []
for i in range(len(f_values)):
    profit_values.append(h(X_values[i],f_values[i]))
    
plt.plot(f_values, profit_values)

profit_max = max(profit_values)
i = profit_values.index(profit_max)
optimum_f = f_values[i]

print(optimum_f)