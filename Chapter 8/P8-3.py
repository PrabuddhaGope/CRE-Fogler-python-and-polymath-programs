from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

#Define constants 
k1 = 1
k2 = 100
K1a = 10
K2a = 1.5

#Define odes
def odes(x, t):
    #Assign variables to x vector
    Ca = x[0]
    Cd = x[1]
    Cu = x[2]
    #rate laws
    r1a = -k1 * (Ca - Cd / K1a)
    r2a = -k2 * (Ca - Cu / K2a)
    #relation between rate laws
    r1d = -r1a
    r2u = -r2a
    #mole balances (+ stoichiometry)
    dCadt = r1a + r2a
    dCddt = r1d
    dCudt = r2u
    
    return [dCadt, dCddt, dCudt]

t_values = np.linspace(0, 1, 100000)
x0 = [1, 0, 0]

C_values = odeint(odes, x0, t_values)

Ca_values = C_values[:, 0]
Cd_values = C_values[:, 1]
Cu_values = C_values[:, 2]

print("The maximum value of Cu is {} and occurs at {}".format(Cu_values.max(), t_values[np.argmax(Cu_values)]))
print("The maximum value of Cd is {} and occurs at {}".format(Cd_values.max(), t_values[np.argmax(Cd_values)]))
plt.plot(t_values, Ca_values, label="Ca")
plt.plot(t_values, Cd_values, label="Cd")
plt.plot(t_values, Cu_values, label="Cu")

plt.legend()
plt.show()